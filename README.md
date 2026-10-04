# Felipe Dias · bilingual portfolio

Portuguese is served at `/`, English at `/en/`. Each project has a page in both languages. The language links preserve the current page and work without JavaScript.

## Edit and preview

The editorial source is `portfolio/content.py`. Update facts and translations there. Layout and styles are in `portfolio/build.py` and `portfolio/style.css`.

```sh
python portfolio/build.py
python -m http.server 8765 --directory _site
```

This previews the new portfolio. To also render the retained Quarto pages, install Quarto and the Python packages in `requeriments.txt`, then run:

```sh
quarto render
python portfolio/build.py
```

The existing `learning/` sources remain intact. The GitHub Actions workflow renders the configured Quarto pages, overlays the new portfolio, excludes study notes from publication, and publishes `_site` to the existing `gh-pages` target without rendering a second time.

## PDFs

The site links to `portfolio/downloads/Felipe_Dias_Portfolio_PT.pdf` and `Felipe_Dias_Portfolio_EN.pdf`. Print layouts share the same editorial source:

```sh
python portfolio/build_pdf.py
```

Open the resulting `portfolio/print/portfolio_pt.html` and `portfolio_en.html` with Chromium and print to A4 PDF with background graphics enabled and browser headers/footers disabled. Preserve the filenames above when replacing the downloads. Then rebuild the site.

## Editorial notes

- Gorgona's 42,037 records are a dashboard count on October 3, 2026, across all units and the full period, with the specified class filters. They are not unique patients.
- The two-minute ECG-to-alert observation is from two ECGs in one encounter on May 20, 2026.
- PhysioNet's first place belongs to team AIMED in the classification task. The 0.817 value is the test score reported in the team's paper.
- Scientific metrics, operational counts and case-study timings are kept separate.
- The timeline is an excerpt rendered from the supplied presentation. The published asset omits the patient-identification block.
- Original screenshots and diagrams retain Portuguese interface labels. English captions explain their content.
- The map uses © OpenStreetMap contributors. Location: PA Rodrigo Argolo, CNES 7033850, Rua Pernambuco, Tancredo Neves, Salvador. Registry position: -12.94539, -38.44634.
- Employment dates and Samsung role follow the CV supplied by the author.

Design references: UC Davis DataLab's portfolio workshop and Arthur Koehl's project-based portfolio. The layout and text are original.


Atualização editorial: três projetos selecionados (Gorgona, ECG na emergência do InCor e RPMS). PhysioNet aparece como prêmio no currículo e como origem do modelo do Gorgona. PDF resumido de cinco páginas por idioma. Referências do RPMS ligadas às frentes de qualidade de sinal, pressão arterial, diabetes e sono.

Revisão de 04/10/2026: currículo PT/EN atualizado com Samsung, experiência no InCor, LLMs, competências e premiações. RPMS expandido como Remote Patient Monitoring System. Descrições uniformizadas. Notas de estudo mantidas apenas no código-fonte e excluídas da publicação. Doutorado nomeado conforme o currículo fornecido pelo autor.

Revisão para candidaturas de engenharia: responsabilidades e evidências em destaque, decisões técnicas por projeto e separação entre protótipo, implantação e pesquisa. O fluxo original com IA substitui a ilustração na miniatura do Gorgona. Os diagramas completos permanecem nas páginas dos projetos. Nenhum cargo de Staff ou resultado operacional sem documentação foi acrescentado.
