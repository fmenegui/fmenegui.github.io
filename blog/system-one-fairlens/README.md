# Bias, Refusals and Language in Jev and GPT Decisions

Public research supplement for https://fmenegui.com/blog/system-one-fairlens/.

The article reports all 228,760 completed tasks from the 38 closed FairLens questions on Jev and GPT Decisions, in English and Brazilian Portuguese. The 31 open questions were not executed. The source CSV is unchanged from the audited experiment and contains 104 columns, image identifiers and hashes, prompts, reconstructible requests, saved API responses, choices and scores. No API credentials or complete image bank are distributed.

Download `data/fairlens-responses.csv.gz` for the complete response table or extract `data/fairlens-reproducibility.zip` for the article, eleven illustrated inputs, historical image sources, complete statistics and offline reproduction code. See `reproducibility/README.md` for dependencies and commands. All included files are listed in `checksums.json`.

The analyses are exploratory. Independent human translation review remains pending. Demographic annotations come from the source dataset. The expected answers are logical benchmark targets, not ground truth about the people shown. The original UTKFace research and noncommercial conditions apply to the illustrated inputs. Historical media retain their original attribution and rights.

Build the download archive with `python scripts/build_fairlens_downloads.py` from the website repository root, before `quarto render`. This performs no model calls.
