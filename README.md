# Felipe Dias · bilingual portfolio

Portuguese is served at `/`, English at `/en/`. Each project has a page in both languages. The language links preserve the current page and work without JavaScript.

## Edit and preview

The editorial source is `portfolio/content.py`, with the bilingual PhysioNet 2024 story in `portfolio/challenge.py`. Update facts and translations there. Layout and styles are in `portfolio/build.py` and `portfolio/style.css`.

The layout follows a personal research homepage: a white background, ordinary blue links, a candid portrait and locally hosted Merriweather and Source Sans. Color tokens are defined in `:root` in `portfolio/style.css`. Project thumbnails crop the original diagrams and app screenshots in CSS, leaving the source assets intact. The homepage presents the four research projects. At phone widths, the portrait stays visible and project descriptions use the full content width. Navigation, language switching, and downloads work without JavaScript. There are no decorative animations.

The builder adds content hashes to the stylesheet and PDF URLs so visitors receive revised styles and downloads after deployment. This does not require changing the publishing workflow.

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

- The two-minute ECG-to-alert observation is from two ECGs in one encounter on May 20, 2026.
- PhysioNet's first place belongs to team AIMED in the classification task. The 0.817 value is the test score reported in the team's paper.
- Scientific metrics, operational counts and case-study timings are kept separate.
- The timeline is an excerpt rendered from the supplied presentation. The published asset omits the patient-identification block.
- Original screenshots and diagrams retain Portuguese interface labels. English captions explain their content.
- The map uses © OpenStreetMap contributors. Location: PA Rodrigo Argolo, CNES 7033850, Rua Pernambuco, Tancredo Neves, Salvador. Registry position: -12.94539, -38.44634.
- Employment dates and Samsung role follow the CV supplied by the author.

Design references: UC Davis DataLab's portfolio workshop and Arthur Koehl's project-based portfolio. The layout and text are original.


The website features four projects: Gorgona, InCor emergency ECG classification, PhysioNet Challenge 2024 and RPMS. The PhysioNet page describes the doctoral experiments and AIMED classification method, with the original award photograph and certificate, training stages, official scores, news links and earlier challenge topics. News links identify publication dates and republication sources. Thesis experiments are identified separately from challenge results. The five-page PDF downloads cover the three original projects. RPMS references cover signal quality, blood pressure, diabetes and sleep.

The GitHub project showcase has been removed from both homepages. Portuguese and English copy is written for each language, with shorter explanations and fewer repeated descriptions. The redundant design-choice blocks have been removed because their content is covered in the method and implementation sections. AIMED leadership, original photographs, the CinC 2024 methodology figure and numerical research results are retained.

Copy uses direct descriptions of the author's work in both languages. The Gorgona pages, CV and PDF downloads omit operational counts and references to dashboard queries after July 2026. The original dashboard screenshot remains published, with a descriptive caption that does not state when it was captured.

The CV and project descriptions use first-person accounts of the author's actual work. Felipe led team AIMED and was first author of its PhysioNet 2024 paper. Clicking a photograph or project figure opens its original image. Captions describe and credit the image without separate instructions or links for opening it.

Revisão de 04/10/2026: currículo PT/EN atualizado com Samsung, experiência no InCor, LLMs, competências e premiações. RPMS expandido como Remote Patient Monitoring System. Descrições uniformizadas. Notas de estudo mantidas apenas no código-fonte e excluídas da publicação. Doutorado nomeado conforme o currículo fornecido pelo autor.

Revisão para candidaturas de engenharia: responsabilidades e evidências em destaque, decisões técnicas por projeto e separação entre protótipo, implantação e pesquisa. O fluxo original com IA substitui a ilustração na miniatura do Gorgona. Os diagramas completos permanecem nas páginas dos projetos. Nenhum cargo de Staff ou resultado operacional sem documentação foi acrescentado.
