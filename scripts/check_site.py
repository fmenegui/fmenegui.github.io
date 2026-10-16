#!/usr/bin/env python3
"""Fail publication on broken discovery metadata or missing local resources."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

from site_seo import AUTHOR, ORIGIN, ROOT, SITEMAP_NS, XHTML_NS, Document, alternates, read_pages


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
    assert {urljoin(ORIGIN, x["href"]) for x in search} == urls
    for rel in ["404.html", "cv/cv.html", "projects/ppg.html", "en/projects/ppg.html"]:
        assert "noindex" in Document((output / rel).read_text()).meta["robots"]
    print(f"PASS: {len(pages)} canonical pages, {len(posts)} posts, schemas, languages, local links, RSS and search")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    check(parser.parse_args().output.resolve())
