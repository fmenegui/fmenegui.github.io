#!/usr/bin/env python3
"""Fail publication on broken discovery metadata or missing local resources."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET
from PIL import Image
from lxml import html as H
from hashlib import sha256

from site_seo import AUTHOR, ORIGIN, ROOT, SITEMAP_NS, XHTML_NS, Document, alternates, canonical, read_pages


class Resources(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.targets = []
        self.ids = set()
        self.schemas = []
        self.schema = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        key = {"a": "href", "link": "href", "img": "src", "script": "src"}.get(tag)
        if key and a.get(key):
            self.targets.append((tag, a[key]))
        if tag == "source" and a.get("srcset"):
            self.targets.append((tag, a["srcset"]))
        if tag == "script" and a.get("type") == "application/ld+json":
            self.schema = []

    def handle_data(self, data):
        if self.schema is not None:
            self.schema.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.schema is not None:
            self.schemas.append(json.loads("".join(self.schema)))
            self.schema = None


def check(output):
    pages = read_pages(output)
    urls = {p.url for p in pages}
    assert len(urls) == len(pages), "Duplicate canonical pages"
    sitemap = ET.parse(output / "sitemap.xml").getroot()
    sitemap_urls = {e.text for e in sitemap.findall(f"{{{SITEMAP_NS}}}url/{{{SITEMAP_NS}}}loc")}
    assert sitemap_urls == urls, "Sitemap must cover every public page exactly"
    assert len(sitemap.findall(f"{{{SITEMAP_NS}}}url")) == len(urls)
    assert "Sitemap: " + ORIGIN + "/sitemap.xml" in (output / "robots.txt").read_text()
    resources = {p.path.resolve(): Resources(p.html) for p in pages}
    for page in pages:
        doc = page.doc
        canonical_links = [a["href"] for a in doc.links if a.get("rel") == "canonical"]
        assert canonical_links == [page.url], (page.relative, canonical_links)
        assert doc.meta.get("description"), page.relative
        assert "noindex" not in doc.meta.get("robots", "")
        assert doc.meta.get("og:url") == page.url
        assert doc.meta.get("og:title") == doc.title
        assert doc.meta.get("twitter:title") == doc.title
        assert doc.meta.get("google-site-verification"), page.relative
        expected = alternates(page, urls)
        actual = {a["hreflang"]: a["href"] for a in doc.links if "hreflang" in a}
        assert actual == expected, (page.relative, actual, expected)
        item = next(n for n in sitemap if n.find(f"{{{SITEMAP_NS}}}loc").text == page.url)
        assert {a.attrib["hreflang"]: a.attrib["href"] for a in item.findall(f"{{{XHTML_NS}}}link")} == expected
        resource = resources[page.path.resolve()]
        assert len(resource.schemas) == 1, page.relative
        graph = resource.schemas[0]["@graph"]
        assert any(x.get("@type") == "Person" and x["name"] == AUTHOR for x in graph)
        if page.article:
            article = next(x for x in graph if x["@type"] == "BlogPosting")
            assert article["headline"] == doc.heading
            assert article["datePublished"] == doc.meta["dcterms.date"]
            assert article["mainEntityOfPage"]["@id"] == page.url + "#webpage"
            assert article["image"], page.relative
            for source in doc.sources:
                if source.get("type") != "image/webp":
                    continue
                path = output / urlsplit(source["srcset"]).path.lstrip("/")
                original = path.with_name(path.name.replace(".lossless.webp", ".png"))
                with Image.open(original) as png, Image.open(path) as webp:
                    assert png.size == webp.size, path
                    assert png.convert("RGBA").tobytes() == webp.convert("RGBA").tobytes(), path
                assert path.stat().st_size < original.stat().st_size, path
        for tag, src in resource.targets + [("meta", doc.meta["og:image"])]:
            url = urlsplit(urljoin(page.url, src))
            if url.scheme not in {"http", "https"} or url.netloc != urlsplit(ORIGIN).netloc:
                continue
            target = output / unquote(url.path).lstrip("/")
            if url.path.endswith("/"):
                target /= "index.html"
            assert target.is_file(), f"{page.relative}: missing {tag} resource {src}"
            if tag == "a" and url.fragment and target.suffix == ".html":
                parsed = resources.get(target.resolve())
                if parsed:
                    assert unquote(url.fragment) in parsed.ids, f"{page.relative}: broken fragment {src}"
    posts = {p.url for p in pages if p.article}
    feed = ET.parse(output / "blog/index.xml")
    assert {n.text for n in feed.findall("channel/item/link")} == posts
    search = json.loads((output / "search.json").read_text())
    assert len(search) == len(pages)
    assert {canonical(x["href"]) for x in search} == urls
    for entry in search:
        assert not entry["href"].startswith("/"), "Quarto search requires paths relative to the site root"
        assert "//" not in entry["href"], entry
        target_page = next(p for p in pages if p.relative == entry["objectID"])
        assert entry["title"] == target_page.doc.title
        # Exercise the root offset Quarto applies on every page, not just home.
        for page in pages:
            offset = "../" * (len(Path(page.relative).parts) - 1)
            result = urlsplit(urljoin(page.url, offset + entry["href"]))
            assert "//" not in result.path, (page.relative, entry)
            assert canonical(result.path.lstrip("/")) in urls, (page.relative, entry)
    # Shared UI must work at every nesting depth and use the same fresh index.
    index_paths = set()
    for page in pages:
        dom = H.fromstring(page.path.read_text())
        assert len(dom.xpath('//main[@id="main"]')) == 1, page.relative
        assert len(dom.xpath('//header[@class="header"]')) == 1, page.relative
        assert len(dom.xpath('//dialog[@id="site-search"]')) == 1, page.relative
        assert dom.xpath('//button[@data-search-open]'), page.relative
        assert not dom.xpath('//*[@id="quarto-header"]'), page.relative
        index_path = dom.find('body').get('data-search-index')
        index_paths.add(index_path)
        assert (output / index_path.lstrip('/')).is_file(), index_path
        if page.article:
            main = dom.xpath('//main')[0]
            assert main.get('lang') == 'en'
            assert dom.xpath('//*[@data-ui-language="pt"]')
            assert all(img.xpath('ancestor::a[@href]') for img in main.xpath('.//img[@src]'))
            for original in (ROOT / Path(page.relative).parent).glob('*'):
                if original.suffix == '.svg' or (original.name.startswith('example') and original.suffix in {'.png', '.json'}):
                    published = output / original.relative_to(ROOT)
                    assert published.read_bytes() == original.read_bytes(), original
    assert len(index_paths) == 1, 'Every page must use the same search revision'
    index_path = index_paths.pop()
    payload = (output / index_path.lstrip('/')).read_bytes()
    assert sha256(payload).hexdigest()[:12] in index_path
    assert len(json.loads(payload)) == len(pages)
    newest = sorted((p for p in pages if p.article),key=lambda p:p.doc.meta['dcterms.date'],reverse=True)
    for rel in ['index.html','en/index.html','blog/index.html']:
        dom = H.fromstring((output / rel).read_text())
        links = dom.xpath('//article[contains(@class,"blog-preview")]/*[self::h2 or self::h3]/a/@href')
        assert links == [urlsplit(p.url).path for p in newest[:3]], rel

    not_found = H.fromstring((output / '404.html').read_text())
    assert not_found.find('body').get('data-search-index') == index_path
    for href in not_found.xpath('//a/@href'):
        target = urlsplit(urljoin(ORIGIN+'/404.html', href))
        if target.netloc == urlsplit(ORIGIN).netloc:
            local = output / target.path.lstrip('/')
            if target.path.endswith('/'):
                local /= 'index.html'
            assert local.is_file(), href

    for rel in ["404.html", "cv/cv.html", "projects/ppg.html", "en/projects/ppg.html"]:
        assert "noindex" in Document((output / rel).read_text()).meta["robots"]
    print(f"PASS: {len(pages)} canonical pages, {len(posts)} posts, schemas, languages, local links, RSS and search")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    check(parser.parse_args().output.resolve())
