"""Add a static BibTeX export to every dated blog post."""
from datetime import date
from html import escape
from pathlib import PurePosixPath
import re

from lxml import html as H
from site_seo import AUTHOR, Document, canonical


def tex_escape(value):
    replacements = {
        "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
        "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return re.sub(r"[\\{}&%$#_~^]", lambda match: replacements[match[0]], value)


def add_citation(root, main, path, relative):
    doc = Document(H.tostring(root, encoding="unicode"))
    if not doc.meta.get("dcterms.date"):
        return
    published = date.fromisoformat(doc.meta["dcterms.date"][:10])
    slug = PurePosixPath(relative).parent.name
    key = f"dias{published.year}-{slug}"
    authors = root.xpath('//meta[@name="author"]/@content') or [AUTHOR]
    names = []
    for author in authors:
        parts = author.rsplit(" ", 1)
        names.append(author if "," in author or len(parts) == 1 else f"{parts[1]}, {parts[0]}")
    fields = {
        "author": tex_escape(" and ".join(names)),
        "title": "{" + tex_escape(doc.heading) + "}",
        "year": str(published.year),
        "month": str(published.month),
        "howpublished": "Blog post",
        "url": canonical(relative),
        "note": f"Published on {published.isoformat()}",
    }
    bibtex = "@misc{" + key + ",\n" + ",\n".join(
        f"  {name} = {{{value}}}" for name, value in fields.items()
    ) + "\n}\n"
    path.with_name("citation.bib").write_text(bibtex, encoding="utf-8")
    # Replace our own block when rebuilding an already enhanced page.
    for old in main.xpath('./details[@id="cite-this-post"]'):
        old.drop_tree()
    main.append(H.fragment_fromstring(f'''
<details class="post-citation" id="cite-this-post">
  <summary data-i18n="cite-post">Cite this post</summary>
  <p data-i18n="citation-help">Copy this entry into your .bib file.</p>
  <pre tabindex="0" aria-label="BibTeX"><code id="post-bibtex">{escape(bibtex)}</code></pre>
  <div class="citation-actions">
    <button type="button" hidden data-copy-citation="post-bibtex" data-i18n="copy-bibtex">Copy BibTeX</button>
    <a href="citation.bib" download="{key}.bib" data-i18n="download-bibtex">Download .bib</a>
  </div>
  <p class="citation-usage"><span data-i18n="cite-latex">In LaTeX, use</span> <code>\\cite{{{key}}}</code>.</p>
  <p class="citation-status" data-citation-status role="status" aria-live="polite"></p>
</details>'''))
    head = root.find("head")
    for old in head.xpath('./link[@type="application/x-bibtex"]'):
        old.drop_tree()
    head.append(H.Element("link", rel="alternate", type="application/x-bibtex",
                          href=canonical(relative) + "citation.bib", title="BibTeX"))
