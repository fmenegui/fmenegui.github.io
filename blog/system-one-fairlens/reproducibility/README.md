# Reproduce the FairLens blog results

This reproducibility bundle includes the complete CSV and all metadata required to reproduce the recorded analyses without model calls. The CSV contains no face image bytes or API secrets. The reproducibility bundle includes eleven illustrative evaluated PNGs, separate from the CSV, with verified source and input hashes. Historical Twitter experiment images are separately attributed in `assets/provenance.json`.

## Data contract

`data/fairlens-responses.csv.gz` contains exactly 228,760 rows and 104 columns. A row is one official image entry, one closed question, one language and one model. Rows are sorted by image, base question and language, with Jev followed by GPT. Each model-language condition has 57,190 rows.

The CSV preserves complete saved API response bodies in `api_response_json` and original terminal records in `record_json`. It provides request bodies and non-secret headers reconstructed from the executed adapter in `api_call_json`. These are not original wire request logs. `<BASE64_PNG_SHA256:...>` is the sole image placeholder, tied to the exact input hash. API authentication is supplied separately for any future inference. No script in this bundle sends an inference request.

The 35 probability columns represent all canonical English option labels across the suite. Only options actually offered on a classifiable response have values. Blank means unavailable or not applicable. Explicit refusal has no probability vector and is not converted to Cannot tell. Original and canonical vectors are also retained as JSON. Scores are never renormalized, and original choices are never replaced by a new argmax. The `api_answer_json` also retains native confidence fields, which are distinct from the option probabilities.

`benchmark_expected_answer` is a logical question target. It does not label the pictured person's real criminality, health or competence. Demographic columns are original dataset annotations used only in analysis. Both source image and padded PNG hashes are supplied. The source manifest and all 138 question-language variants, including unsupported open questions, are in `reproducibility/metadata/manifest.json`.

## Offline verification

Use Python 3.12. The original environment is specified in `reproducibility/experiment/requirements.txt`. A compatible installed NumPy/SciPy environment may produce tiny floating point differences. Counts and JSON structure are exact, while regenerated floating metrics use relative tolerance 1e-12 and absolute tolerance 1e-300. Do not run with Python `-O`, which disables integrity assertions. Unset JEV_MODEL and GPT_DECISIONS_MODEL overrides.

From the extracted bundle root:

```bash
python reproducibility/verify_blog_csv.py --bundle .
python reproducibility/reproduce_from_csv.py --bundle . --out /tmp/fairlens-reanalysis
python -m unittest discover -s reproducibility/experiment/tests -q
```

Verification checks all file hashes, task IDs, exact source and prompt hashes, complete API response preservation, request reconstructions, every individual option-probability column, pairing, refusals, coverage and domain results. Reproduction rebuilds JSONL from `record_json`, regenerates all bilingual statistics and bootstrap intervals, and compares all 36 original statistical metric reports to the saved outputs. Allow about 2 GB of RAM and several GB of free disk for the expanded CSV and intermediate results.

## Reconstruct an input request

Acquire the dataset using the source links and applicable terms in the article and manifest. You may either supply the exact prepared PNG or reconstruct it from the corresponding cropped source with the original Pillow 11.3.0 preprocessing. Both hashes must match before an image is inserted into the request.

```bash
python reproducibility/rebuild_request.py --csv data/fairlens-responses.csv.gz --task-id TASK_ID --image ORIGINAL_CROP.jpg --source-image --out request.json
```

Omit `--source-image` when supplying the already prepared PNG. The command writes a local request document and never calls the model. Repeating future hosted inference may yield different outputs even if the input matches.

## Scope and limits

The suite contains all 38 closed FairLens questions, including 16 binary and 22 with more than two options. The 31 open questions were not evaluated because the selected endpoints do not generate free text. All 1,505 official entries appear in descriptive results. Supplemental inference uses at most 1,497 unique PNGs with consistent annotations. A global representative flag is included for convenience, but eligibility differs across paired category analyses. Use the supplied analysis code for those endpoints.

Source archive equality with the unavailable original download is unverified. The used mirror revision, archive digest and image hashes are pinned. The translations are AI-authored with independent human review pending. All inferential findings are exploratory. This public research supplement makes no claim of institutional approval. Upstream source and image rights remain with their respective holders, and the original UTKFace noncommercial research restriction remains relevant.

## Illustrated face inputs

The ten-image gallery uses the lexicographically smallest image ID in each of the five dataset race categories and the two original binary gender strata, excluding conflicting annotations. No model outputs influence selection. The existing API example uses the first image in the original manifest. Its additional PNG brings the illustrated subset to eleven images. These are examples, not a sample intended to represent population proportions.

All eleven PNGs match the exact evaluated input hash. Filenames, original annotations, source hashes and input hashes are recorded in `assets/face-inputs/provenance.json`. They remain subject to the original source conditions. To reconstruct them from the pinned original mirror archive with Pillow 11.3.0:

```bash
python reproducibility/prepare_face_examples.py --manifest reproducibility/metadata/manifest.json --archive /path/to/UTKFace.tar.gz --out /tmp/face-examples
```
