# FairLens replication manuscript and review package

This is an exploratory replication of **all 38 closed questions**, not the full 69 question evaluation. The manuscript, analysis code and review materials cover 1,505 official image entries, two languages and two model endpoints. The final consolidated set has 228,760 terminal tasks, including 16,761 explicit GPT refusals. No new paid inference is required to audit or reproduce the results.

## Contents

- `manuscript.md` is the editable scientific manuscript in English. It distinguishes all task soundness, category coverage and conditional correctness.
- `audit_release.py` losslessly consolidates the final Actions artifact and checks each raw response, task hash, served version, option label and probability vector.
- `verify_release.py` verifies a prepared package offline and can regenerate the complete bilingual analysis and all 36 original metric outputs.
- `prepare_materials.py` creates figures, complete question tables and a human translation review packet. It also assembles the private review package.
- `build_manuscript.py` builds the Word manuscript from Markdown. Document rendering requires LibreOffice and the document renderer used for visual QA, separately from analysis dependencies.

The prepared ZIP also contains `data/responses.jsonl`, with exactly one lossless terminal record per task, and `data/observations.csv`, with normalized English category labels. The manifest includes all 138 question language variants and provenance. It includes no image bytes or authentication material. Request templates are reconstructed from executed code, not retained original wire requests.

## Reproduce without model calls

Extract the review ZIP and use Python 3.12. Install its `code/requirements.txt`, or use a compatible environment with NumPy and SciPy. From the extracted package:

```bash
python code/publication/verify_release.py --package .
python code/publication/verify_release.py --package . --full-out /tmp/fairlens-reanalysis
python -m unittest discover -s code/tests -v
```

The first command verifies file hashes, all tasks, raw normalization, domain counts and all 260 exact paired tests and their Holm correction. The second also regenerates bootstrap intervals and all 36 unmodified upstream reports. Structure and counts must match exactly. Floating results allow a relative tolerance of 1e-12 to accommodate numerical library differences, with absolute tolerance 1e-300. Neither command calls an inference endpoint. The complete JSONL expands to hundreds of MB, so allow at least 2 GB of RAM and 2 GB of free disk space. Do not run Python with `-O`, which disables integrity assertions. Unset model override environment variables.

For a new consolidation from the archived original workflow artifact, place `source-artifact.zip` next to the final `metrics-bilingual.json`, then run:

```bash
python publication/audit_release.py --artifact /path/source-artifact.zip --out /path/exported-data
```

Source artifact ID: 12068891258. Workflow run: 38936918025. Artifact SHA256: cef87a83cc6096aa54fdbf9925882fd2e65723cbb947f111c9a2dee35831a23f.

The manifest records the pinned image mirror and original source hashes. Reconstructing images requires dataset access and terms. It is separate from offline analysis. Historical aliases are not a guarantee of reproducible future model calls.

## Denominators and known interface observations

Descriptive and original metric tables retain 1,505 official entries. Supplemental inference uses at most 1,497 unique PNG inputs with consistent demographic annotations. Exact duplicate photographs do not establish unique person identities. Soundness with all terminal responses treats refusals as nonmatches. Conditional category metrics exclude refusals, while Cannot tell is an ordinary benchmark category. Original metric scripts retain refusal markers in their denominators. The association script counts them as unparsed, outside both its neutral and nonneutral counts. Refusals can therefore reduce its association rate denominator ratio without constituting neutral decisions. Use the explicit outcome decomposition when interpreting association rates.

All 211,999 category responses have complete finite vectors accepted by the executed tolerance of sum within 0.02 of one. The audit separately discloses 612 Jev vectors whose sums differ from one by more than 1e-9, with maximum discrepancy 0.01, and 11 Jev choices 0.01 below the displayed maximum probability. Raw choices are retained. No score is silently normalized and no choice is replaced by a recomputed argmax. All displayed probability values have at most two decimals. The corresponding GPT discrepancy counts are zero. These are observed contract precision limitations, not evidence of a cause.

The 3,600 legacy records lacking explicit language and domain fields remain unchanged in raw JSONL. Their CSV metadata is derived from the matching question ID, prompt hash and v2 task identity. Duplicate checkpoint records agree on raw terminal bodies. Checkpoint line counts are not unique trial counts and are not a complete history of every HTTP request.

## Human review and release status

The translation packet includes all 69 EN/PT question pairs, context prompts and suffixes. Every human review status starts as pending, including the 31 questions not executed. Structural checks and AI review do not substitute for independent bilingual review. Reviewers should assess semantics without seeing model outcomes where practical. Proposed corrections must be saved separately and versioned. Any rerun using changed prompts requires a separate experiment.

Before submission, human authors must confirm translations, the interpretation of the benchmark expected labels, authorship, affiliations, funding, conflicts and the appropriate institutional review statement. Before public distribution, confirm dataset and third party reuse conditions. The pinned upstream source tree contains no separate LICENSE file, and its README specifies noncommercial research conditions for UTKFace. The review package preserves source provenance and does not grant additional rights. No submission, public release or claim of institutional approval has been made.

All inferential findings are exploratory because interim analyses occurred. Holm correction covers the declared 260 categorical language tests. Score, racial subgroup and interaction intervals are not adjusted. This design does not identify causal effects of race, language independent of wording, or model architecture.
