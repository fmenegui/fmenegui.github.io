#!/usr/bin/env python3
"""Add discovery metadata to final HTML without changing editorial content.

Run after Quarto and the bilingual portfolio overlay. Uses rendered titles,
descriptions, dates, images and text, never a second copy of article content.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, datetime, timezone
from email.utils import format_datetime
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://fmenegui.com"
AUTHOR = "Felipe Meneguitti Dias"
VERIFICATION = "h6HccuHaE3NZCaV6t7jhLx1lPqosFyi3aunJcjO5xSQ"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
IMAGE_NS = "http://www.google.com/schemas/sitemap-image/1.1"
XHTML_NS = "http://www.w3.org/1999/xhtml"
ET.register_namespace("", SITEMAP_NS)
ET.register_namespace("image", IMAGE_NS)
ET.register_namespace("xhtml", XHTML_NS)


class Document(HTMLParser):
    """Read metadata and visible content without serializing the document."""

    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.meta = {}
        self.links = []
        self.images = []
        self.sources = []
        self.scripts = []
        self.title_parts = []
        self.h1_parts = []
        self.body_parts = []
        self.main_parts = []
        self.paragraphs = []
        self.paragraph = None
        self.lang = "en"
        self.in_title = self.in_h1 = self.in_body = self.in_main = False
        self.ignored = 0
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang", "en")
        if tag == "meta":
            self.meta[a.get("name", a.get("property", a.get("http-equiv", ""))).lower()] = a.get("content", "")
        if tag == "link":
            self.links.append(a)
        if tag == "img":
            self.images.append(a)
        if tag == "source":
            self.sources.append(a)
        if tag == "script":
            self.scripts.append(a)
        if tag in {"script", "style"}:
            self.ignored += 1
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.in_h1 = True
        if tag == "body":
            self.in_body = True
        if tag == "main":
            self.in_main = True
        if tag == "p" and self.in_main:
            self.paragraph = []

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.ignored = max(0, self.ignored - 1)
        if tag == "title":
            self.in_title = False
        if tag == "h1":
            self.in_h1 = False
        if tag == "body":
            self.in_body = False
        if tag == "main":
            self.in_main = False
        if tag == "p" and self.paragraph is not None:
            self.paragraphs.append(self.text(self.paragraph))
            self.paragraph = None

    def handle_data(self, data):
        if self.ignored:
            return
        if self.in_title:
            self.title_parts.append(data)
        if self.in_h1:
            self.h1_parts.append(data)
        if self.in_body:
            self.body_parts.append(data)
        if self.in_main:
            self.main_parts.append(data)
        if self.paragraph is not None:
            self.paragraph.append(data)

    @staticmethod
    def text(parts):
        return re.sub(r"\s+", " ", " ".join(parts)).strip()

    @property
    def title(self):
        return self.text(self.title_parts)

    @property
    def heading(self):
        return self.text(self.h1_parts) or self.title

    @property
    def visible_text(self):
        return self.text(self.body_parts)


def canonical(relative: str) -> str:
    if relative.endswith("index.html"):
        relative = relative[:-len("index.html")]
    return ORIGIN + "/" + relative


@dataclass
class Page:
    path: Path
    relative: str
    html: str
    doc: Document
    images: list[str]

    @property
    def url(self):
        return canonical(self.relative)

    @property
    def article(self):
        return self.relative.startswith("blog/") and bool(self.doc.meta.get("dcterms.date"))

    @property
    def description(self):
        return self.doc.meta.get("description") or next((p for p in self.doc.paragraphs if p), "")


def local_file(output: Path, page_url: str, src: str) -> Path | None:
    url = urlsplit(urljoin(page_url, src))
    if url.netloc != urlsplit(ORIGIN).netloc:
        return None
    target = (output / unquote(url.path).lstrip("/")).resolve()
    if not target.is_relative_to(output.resolve()):
        return None
    return target if target.is_file() else None


def read_pages(output: Path) -> list[Page]:
    pages = []
    for path in sorted(output.rglob("*.html")):
        rel = path.relative_to(output).as_posix()
        if rel == "404.html" or rel.startswith(("site_libs/", "learning/")):
            continue
        html = path.read_text(encoding="utf-8")
        doc = Document(html)
        if "refresh" in doc.meta or "noindex" in doc.meta.get("robots", "").lower():
            continue
        if not doc.title:
            raise ValueError(f"Missing existing title in {rel}")
        images = []
        for img in doc.images:
            src = img.get("src", "")
            if src and local_file(output, canonical(rel), src):
                url = urljoin(canonical(rel), src)
                if url not in images:
                    images.append(url)
        pages.append(Page(path, rel, html, doc, images))
    return pages


def alternates(page: Page, urls: set[str]) -> dict[str, str]:
    if page.relative.startswith("blog/"):
        return {}
    rel = page.relative.removeprefix("en/")
    pt, en = canonical(rel), canonical("en/" + rel)
    if pt in urls and en in urls:
        return {"pt-BR": pt, "en": en, "x-default": pt}
    return {}


def schema(page: Page, articles: list[Page]) -> dict:
    person = {"@type": "Person", "@id": ORIGIN + "/#person", "name": AUTHOR,
              "url": ORIGIN + "/about.html"}
    website = {"@type": "WebSite", "@id": ORIGIN + "/#website",
               "url": ORIGIN + "/", "name": "Felipe Dias", "publisher": {"@id": person["@id"]}}
    web = {"@type": "WebPage", "@id": page.url + "#webpage", "url": page.url,
           "name": page.doc.title, "description": page.description, "inLanguage": page.doc.lang,
           "isPartOf": {"@id": website["@id"]}}
    graph = [person, website, web]
    if page.relative.endswith("about.html"):
        web.update({"@type": "ProfilePage", "mainEntity": {"@id": person["@id"]}})
    if page.relative == "blog/index.html":
        web["@type"] = "CollectionPage"
        web["mainEntity"] = {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": p.url, "name": p.doc.heading}
            for i, p in enumerate(articles)]}
    if page.article:
        article = {"@type": "BlogPosting", "@id": page.url + "#article", "url": page.url,
                   "mainEntityOfPage": {"@id": web["@id"]}, "headline": page.doc.heading,
                   "description": page.description, "author": {"@id": person["@id"]},
                   "datePublished": page.doc.meta["dcterms.date"], "inLanguage": page.doc.lang,
                   "isAccessibleForFree": True, "image": page.images}
        graph.append(article)
        crumbs = [(ORIGIN + "/", "Felipe Dias"), (ORIGIN + "/blog/", "Blog"),
                  (page.url, page.doc.heading)]
        graph.append({"@type": "BreadcrumbList", "@id": page.url + "#breadcrumb",
                      "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                           "item": url, "name": name}
                                          for i, (url, name) in enumerate(crumbs)]})
        web["breadcrumb"] = {"@id": page.url + "#breadcrumb"}
    return {"@context": "https://schema.org", "@graph": graph}


def optimize_images(html: str, page: Page, output: Path) -> str:
    """Offer pixel-identical WebP copies, preserving original PNG fallbacks."""
    # Unwrap our own output so repeated builds never nest picture elements.
    html = re.sub(r'<picture data-lossless>\s*<source\b[^>]*>\s*(<img\b[^>]*>)\s*</picture>',
                  r'\1', html, flags=re.I)

    def update(match):
        tag = match.group(0)
        parser = Document(tag)
        attrs = parser.images[0]
        additions = []
        target = local_file(output, page.url, attrs.get("src", ""))
        if target and target.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            with Image.open(target) as image:
                width, height = image.size
            if "width" not in attrs and "height" not in attrs:
                additions.extend([f'width="{width}"', f'height="{height}"'])
        if "decoding" not in attrs:
            additions.append('decoding="async"')
        # Preserve hero loading priority. Blog figures occur after the opening text.
        if page.article and "loading" not in attrs:
            additions.append('loading="lazy"')
        if additions:
            ending = "/>" if tag.endswith("/>") else ">"
            tag = tag[:-len(ending)].rstrip() + " " + " ".join(additions) + ending
        if page.article and target and target.suffix.lower() == ".png":
            optimized = target.with_suffix(".lossless.webp")
            with Image.open(target) as original:
                original.save(optimized, "WEBP", lossless=True, method=6, exact=True)
                with Image.open(optimized) as compressed:
                    if original.convert("RGBA").tobytes() != compressed.convert("RGBA").tobytes():
                        raise ValueError(f"Image pixels changed: {optimized}")
            if optimized.stat().st_size < target.stat().st_size:
                src = "/" + optimized.relative_to(output).as_posix()
                return f'<picture data-lossless><source srcset="{escape(src, quote=True)}" type="image/webp">{tag}</picture>'
            optimized.unlink()
        return tag
    return re.sub(r"<img\b[^>]*>", update, html, flags=re.I)


def enrich(page: Page, pages: list[Page], output: Path):
    head_end = re.search(r"</head\s*>", page.html, re.I)
    if head_end is None:
        raise ValueError(f"Missing head in {page.relative}")
    head = page.html[:head_end.start()]
    rest = page.html[head_end.start():]
    head = re.sub(r"\n?<!-- site-discovery:start -->.*?<!-- site-discovery:end -->\n?", "", head,
                  flags=re.S)
    # Replace only managed discovery tags, leaving existing titles/copy intact.
    def keep_tag(match):
        tag = match.group(0)
        parser = Document(tag)
        if parser.meta:
            key = next(iter(parser.meta))
            if key.startswith(("og:", "twitter:", "article:")) or key in {"robots", "google-site-verification"}:
                return ""
        if parser.links:
            attrs = parser.links[0]
            if attrs.get("rel") == "canonical" or "hreflang" in attrs:
                return ""
            if attrs.get("type") == "application/rss+xml":
                return ""
        return tag
    head = re.sub(r"<(?:meta|link)\b[^>]*>", keep_tag, head, flags=re.I)
    head = re.sub(r'<script\b[^>]*\bid="site-discovery"[^>]*>.*?</script>', "", head,
                  flags=re.I | re.S)
    tags = []
    def meta(key, value, property=False):
        attr = "property" if property else "name"
        tags.append(f'<meta {attr}="{key}" content="{escape(value, quote=True)}">')
    if not page.description:
        raise ValueError(f"Missing existing description/introductory paragraph in {page.relative}")
    if not Document(head).meta.get("description"):
        meta("description", page.description)
    tags.append(f'<link rel="canonical" href="{page.url}">')
    for lang, url in alternates(page, {p.url for p in pages}).items():
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="{url}">')
    tags.append(f'<link rel="alternate" type="application/rss+xml" title="Blog | Felipe Dias" href="{ORIGIN}/blog/index.xml">')
    meta("robots", "index, follow, max-image-preview:large")
    meta("google-site-verification", VERIFICATION)
    image = page.images[0] if page.article and page.images else ORIGIN + "/assets/felipe.jpg"
    for key, value in {"og:site_name": "Felipe Dias", "og:title": page.doc.title,
                       "og:description": page.description, "og:url": page.url,
                       "og:type": "article" if page.article else "website",
                       "og:locale": page.doc.lang.replace("-", "_"), "og:image": image,
                       "og:image:alt": page.doc.heading}.items():
        meta(key, value, True)
    for key, value in {"twitter:card": "summary_large_image", "twitter:title": page.doc.title,
                       "twitter:description": page.description, "twitter:image": image,
                       "twitter:image:alt": page.doc.heading}.items():
        meta(key, value)
    if page.article:
        meta("article:published_time", page.doc.meta["dcterms.date"], True)
        meta("article:author", ORIGIN + "/about.html", True)
    articles = sorted((p for p in pages if p.article),
                      key=lambda p: p.doc.meta["dcterms.date"], reverse=True)
    data = json.dumps(schema(page, articles), ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    tags.append(f'<script id="site-discovery" type="application/ld+json">{data}</script>')
    html = head.rstrip() + "\n<!-- site-discovery:start -->\n" + "\n".join(tags) + "\n<!-- site-discovery:end -->\n" + rest
    html = optimize_images(html, page, output)
    if Document(html).visible_text != page.doc.visible_text:
        raise ValueError(f"Visible content changed in {page.relative}")
    page.path.write_text(html, encoding="utf-8")


def write_sitemap(pages: list[Page], output: Path):
    root = ET.Element(f"{{{SITEMAP_NS}}}urlset")
    urls = {p.url for p in pages}
    for page in pages:
        node = ET.SubElement(root, f"{{{SITEMAP_NS}}}url")
        ET.SubElement(node, f"{{{SITEMAP_NS}}}loc").text = page.url
        # Omit lastmod rather than treating a rebuild as a content update.
        for lang, url in alternates(page, urls).items():
            ET.SubElement(node, f"{{{XHTML_NS}}}link", rel="alternate", hreflang=lang, href=url)
        for image in page.images:
            item = ET.SubElement(node, f"{{{IMAGE_NS}}}image")
            ET.SubElement(item, f"{{{IMAGE_NS}}}loc").text = image
    ET.indent(root)
    ET.ElementTree(root).write(output / "sitemap.xml", encoding="utf-8", xml_declaration=True)


def write_feed(pages: list[Page], output: Path):
    root = ET.Element("rss", version="2.0")
    channel = ET.SubElement(root, "channel")
    for key, value in {"title": "Blog | Felipe Dias", "link": ORIGIN + "/blog/",
                       "description": next(p.description for p in pages if p.relative == "blog/index.html"),
                       "language": "en"}.items():
        ET.SubElement(channel, key).text = value
    for page in sorted((p for p in pages if p.article),
                       key=lambda p: p.doc.meta["dcterms.date"], reverse=True):
        item = ET.SubElement(channel, "item")
        for key, value in {"title": page.doc.heading, "link": page.url,
                           "description": page.description}.items():
            ET.SubElement(item, key).text = value
        ET.SubElement(item, "guid", isPermaLink="true").text = page.url
        day = date.fromisoformat(page.doc.meta["dcterms.date"][:10])
        ET.SubElement(item, "pubDate").text = format_datetime(datetime(day.year, day.month, day.day, tzinfo=timezone.utc))
    ET.indent(root)
    ET.ElementTree(root).write(output / "blog/index.xml", encoding="utf-8", xml_declaration=True)


def build(output: Path):
    pages = read_pages(output)
    for page in pages:
        enrich(page, pages, output)
    write_sitemap(pages, output)
    write_feed(pages, output)
    (output / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: " + ORIGIN + "/sitemap.xml\n", encoding="utf-8")
    (output / "search.json").write_text(json.dumps([
        # Quarto prepends each page's relative root offset. A leading slash
        # becomes '..//blog/...' and leaks duplicate path separators into links.
        {"objectID": p.relative, "href": urlsplit(p.url).path.lstrip("/") or "index.html", "title": p.doc.title,
         "section": "", "text": p.doc.text(p.doc.main_parts or p.doc.body_parts)} for p in pages
    ], ensure_ascii=False), encoding="utf-8")
    # Legacy URLs still redirect for readers but must not become search results.
    for rel in ["404.html", "cv/cv.html", "projects/ppg.html", "en/projects/ppg.html"]:
        path = output / rel
        if path.is_file():
            html = path.read_text(encoding="utf-8")
            if 'name="robots"' not in html:
                robot = '<meta name="robots" content="noindex, follow">'
                if '<meta charset="utf-8">' in html:
                    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + robot, 1)
                else:
                    html = robot + html
                path.write_text(html, encoding="utf-8")
    print(f"Discovery metadata verified for {len(pages)} pages, including {sum(p.article for p in pages)} posts")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    build(parser.parse_args().output.resolve())
