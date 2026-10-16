# ECG blog figures and examples

Both ECG articles use `ecg_figures.py`, adapted from the CODE Test journal
figure implementation. The renderer shares fonts, palette, panel spacing,
empirical ROC steps, PCHIP calibration, log-count histograms and interval
conventions. The number of diagnostic classes and histogram count range adapt
to the dataset.

```bash
python blog/ecg_figures.py
python blog/build_ecg_examples.py
quarto render
```

`chart-data.json` stores aggregate coordinates, score histogram counts, AUROC,
Brier and bootstrap bands from saved inference results. The renderer does not
call either model or estimate uncertainty from interpolated curves.
CODE uses 1,000 class-stratified bootstrap samples. PTB-XL uses 300 paired
patient-cluster samples, preserving repeated ECGs from a patient together.
The same resamples are used for both models.

To regenerate aggregates from the original run exports, install scikit-learn
in addition to the website requirements, then run:

```bash
python blog/ecg_figures.py --prepare --jev CODE_JEV.zip --gpt CODE_GPT.zip --ptbxl PTBXL.jsonl
```

Each CODE ZIP must contain one `predictions.jsonl`. PTB-XL JSONL must contain
one record per ECG, with both models' saved answers and patient identifiers.
Individual evaluation records remain private. Only aggregate curves and the
four explicitly selected illustrative answer objects are published.

The examples are CODE `ecg_0` and `ecg_1`, and PTB-XL IDs 1 and 8. These are
the first CODE input and first LBBB-positive input, and the first PTB-XL input
and first MI-positive input. They illustrate outputs, not sample-wide accuracy.
`ecg-examples.json` links each pinned PNG to its saved answer JSON and SHA-256.
PTB-XL PNG hashes match the hashes recorded at inference. CODE did not record
input hashes, so its PNGs were recreated with the original preprocessing and
checked against the recorded dimensions.

`build_ecg_examples.py` verifies the pinned images and matching JSONs offline.
Publishing does not depend on downloading examples from external datasets.
The JSON `answers` objects preserve the stored model fields. They are not
complete HTTP response payloads. Benchmark labels are separate evaluation
metadata and were never included in the classification requests.
