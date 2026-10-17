## All 38 questions with reports by group

## Completed closed suite and publication materials

The final run `38936918025` completed all 228,760 EN/PT tasks across the 38 closed questions, 1,505 official entries and both endpoints. There are 211,999 category responses and 16,761 explicit GPT refusals, with no pending task. The 31 open questions remain unsupported. Earlier smoke and pilot entries below describe historical stages, not the final scope.

The [publication directory](publication/README.md) contains the English scientific manuscript, offline audit and reproduction commands, figures builder and pending independent translation review materials. Final aggregate evidence is in `publication/results/`. All 39 offline tests pass. The prepared review package preserves every terminal raw response without including image bytes or credentials. No new paid inference, submission or public release was performed for manuscript preparation.

The current requested scope is again the complete closed suite of 38 questions, 1,505 entries, two languages and two models, totaling 228,760 tasks. The five-question continuation remains a priority batch and its responses are merged before completing the remaining tasks. The grouped workflow waits for that active continuation, reuses exact checkpoints and then completes eight disjoint thematic groups with at most two workers. Each group publishes an immediate coverage-aware report. A final report pools every group and recomputes the global language-test correction, including explicit refusals as a separate endpoint. Earlier partial results stay labeled exploratory. See `GROUPED-PROTOCOL.md`.

## Five priority legal questions

The current continuation focuses on legal-07 (criminality), legal-02 (suspicion), legal-04 (violence), legal-03 (additional search) and legal-09 (police use of force), retaining all 1,505 official entries and both languages/models. This gives 30,100 tasks. At selection, 25,989 terminal responses could be reused, leaving 1,787 Jev and 2,324 GPT Decisions tasks. The selection follows the initial criminality-bias objective and is exploratory because pilot and partial full-suite data already existed. The full-suite data remain preserved. `fairlens-focused.yml` continues only these missing tasks. Credit exhaustion now stops on the first response instead of being retried as a transient rate limit.

## Full bilingual extension

The 1,505-image, all-domain EN/PT-BR closed suite is described in [PROTOCOL-BILINGUAL.md](PROTOCOL-BILINGUAL.md). There are 38 supported closed and 31 unsupported free-text questions per language. The new workflow is `fairlens-bilingual-full.yml`, with 228,760 paired image-question-model-language tasks. The pilot documentation below remains as a record of the earlier legal-only stage.

# Jev and GPT Decisions: FairLens legal bias audit

Research question: do models make unsupported appearance-based legal judgments, and do the frequency and returned scores differ across the dataset's racial annotations?

This is an audit of model outputs, not a system for predicting criminality. A face has no criminality ground truth. Do not interpret any returned score as a person's probability of being a criminal. No AUROC, calibration against criminal records, or deployment for individual screening is part of this experiment.

## Source and replication scope

- FairLens paper: https://arxiv.org/abs/2609.01691
- Official code: https://github.com/vectorinstitute/fairlens
- Code revision pinned to `130205f243267fc90b973cb875d1711c2d932bbe`
- Exact evaluation image manifest: https://huggingface.co/datasets/vector-institute/fairlens
- Original aligned and cropped images: https://susanqq.github.io/UTKFace/
- Related FAccT 2024 audit: https://arxiv.org/abs/2405.04623

The experiment uses the exact FairLens 1,505-image cropped test manifest, adults aged 25 to 65. Photos are downloaded from UTKFace, not redistributed here. Hugging Face requires the account holder to accept the FairLens conditions. This code does not accept them on the user's behalf or bypass access restrictions. Configure a read-only `HF_TOKEN` after acceptance. UTKFace is restricted to non-commercial research, with underlying image rights retained by their owners. Dataset demographic annotations are imperfect estimates, not verified identity or Brazilian self-declared race categories.

Nine original closed legal questions are loaded from the pinned upstream source. System prefix, question text, option order and expected/adverse labels are preserved. Question `legal-07` is the prespecified primary endpoint: the unsupported choice `Criminal`. Questions 1 through 6 and 9 concern threat, suspiciousness, legal role or force. Question 8 is an object-presence control whose expected label is `No`, not `Cannot tell`.

Both APIs receive identical RGB PNGs. Original crop pixels are preserved without resizing. Use `--min-side 280` for a paired Jev evaluation, adding a centered neutral-gray border to native 200x200 crops. Native-size controls remain available by omitting that option. Source-file and transmitted-PNG SHA-256 hashes are retained. Labels and original filenames are never transmitted. This is an **adaptation to typed Decisions APIs**, not an exact reproduction of the paper's free-text Responses inference. No free-text judge is used in this version. Responses outside the choices, including possible refusals, remain unscored pending human review. They are never silently mapped to `No` or `Cannot tell`.

## Cohorts and budgets

| Mode | Images | Questions | Models | Maximum successful tasks |
|---|---:|---:|---:|---:|
| Technical smoke | 4 | 9 | 2 | 72 |
| Balanced pilot | 200 | 9 | 2 | 3,600 |
| Original complete split | 1,505 | 9 | 2 | 27,090 |

The pilot draws only from the original test split. It balances Black/White annotations and binary dataset gender, matching race counts within 10-year age bands and gender. Fixed seed: 20261016. It is a matched subset, not the complete original split. Full mode keeps all racial groups and original composition. Matching does not remove all differences in illumination, expression, clothing or other features and does not establish a causal effect of race.

Tasks are independently randomized with a fixed seed. Image shards are stable and disjoint. Each image-question-model request is separate so questions do not condition each other. Checkpoints include the image hash, full prompt, choices, model identifier, contract version and repetition in task identity. A changed experiment cannot silently reuse prior successful responses. Keep immutable results folders per cohort and analysis run. Do not run concurrent writers for the same shard.

## Commands

```bash
pip install -r experiments/fairlens-audit/requirements.txt
python experiments/fairlens-audit/audit.py fetch
python experiments/fairlens-audit/acquire_images.py
python experiments/fairlens-audit/audit.py prepare --cohort pilot --n 4 --min-side 280
python experiments/fairlens-audit/audit.py run --dry-run
python experiments/fairlens-audit/audit.py run --max-calls 18
python experiments/fairlens-audit/audit.py analyze
```

Supply existing original cropped images with `prepare --images /path/to/UTKFace`. Matching supports exact original filenames and the original `.jpg.chip.jpg` crop suffix. Missing or duplicate matches fail instead of substituting photos. Preparation validates all 1,505 metadata records even for a pilot.

GitHub Actions reads the repository secret `Hfread_api_key` into the `HF_TOKEN` environment variable.

Credentials follow the existing repository contracts: `JEV_API_KEY`, `OPENAI_API_KEY`, and optional `HF_TOKEN` for source download. Model defaults are the existing repository defaults, `jev-preview` and `gpt-6-luna`. Override with `JEV_MODEL` and `GPT_DECISIONS_MODEL` and retain served model identifiers. API availability and three-way choice support require a live smoke test.

For 200 images, change `--n 200` and use a new `--data` and `--out` folder. For full evaluation use `--cohort full`. Each run requires an explicit `--max-calls`, applied per process. It limits tasks attempted, not billable network calls: a transient failure can cause up to four HTTP attempts per task. Use `--shard 0 --shards 8` through shard 7 for separate batches. Resume against the same output directory. `ok` and `unscored_response` records are terminal. HTTP errors can be retried. Authentication failures stop immediately. The pipeline never automatically starts a full run.

## Analysis

Primary hypothesis: Black minus White difference in the rate of `Criminal` choices for question 7. Report absolute rates, percentage-point difference, ratio when its denominator is nonzero, and 95% image-cluster bootstrap intervals. Secondary analysis compares returned `Criminal` scores only where the complete score vector passes validation. These are API output scores, not calibrated real-world risks. The score scales of different providers may not be comparable.

For every question and group, report expected tasks, scored tasks, unavailable responses, errors, adverse-choice rate, soundness and abstention. Available-case and common-image comparisons across models are both retained. Missingness can itself differ by group and invalidate naive conclusions. Repeated calls are clustered by image in bootstrap resampling. UTKFace has no identity labels, so this does not account for undisclosed repeated identities across different photographs.

Secondary questions are exploratory. Prespecify multiplicity correction before making confirmatory claims about them. Report subgroup sample sizes. A nonsignificant pilot does not establish absence of bias. A similar adverse rate across groups does not establish safe behavior. Do not publish identifiable per-person criminality scores. Review unsupported outputs in a restricted research environment and publish aggregate audit findings.

## Validation and execution status

```bash
python -m unittest discover -s experiments/fairlens-audit/tests -v
```

The workflow performs offline contract/statistics/checkpoint tests and source-access preflight on the audit branch. Manual execution can enable a capped smoke run after data access is configured. Tests use fabricated records and never real appearance-based judgments. They do not establish that either remote API accepts the contract. Live results must be reported separately from these tests.

Outputs are `manifest.json`, per-shard JSONL responses, task plans, `metrics.json`, and `report.md`. Raw face images and API results are ignored by git. GitHub artifacts contain metadata and private model outputs, not face images.

Initial verification on 2026-10-16: 12 offline tests passed, the pinned official nine-question suite parsed, and workflow YAML parsed. The official metadata endpoint returned HTTP 401 without authorized access. GitHub Actions run 38906965089 failed before runner allocation with no executed steps or job logs. No live audit conclusions are available. Configure authorized dataset access and resolve the runner issue before claiming a successful remote smoke test.

Retry on 2026-10-16: GitHub runner allocation and authorized HF download succeeded. The official JSON is keyed by filename rather than the flat list described in the dataset card. Both formats are now supported with strict 1,505-image checks. A thirteenth test covers the observed format. The primary smoke workflow selects four matched images and the unmodified `legal-07` question, for eight API tasks, before a larger pilot. Select question subsets with `prepare --questions legal-07`.

The original Google Drive folder download failed. Primary smoke explicitly selects `acquire_images.py --source hf-mirror`, using `py97/UTKFace-Cropped` revision `e80f21fb21fa3631380c3cb634b79be3ac2f4cba`. Its 106,634,631-byte archive is verified against SHA-256 `2c0655397b498e81b82d685ee74bee8c2e4364a5897caf3afec6ea48929024a7`. Selection still uses the authorized official FairLens filenames. Acquisition source is preserved in a private artifact. Original UTKFace non-commercial research restrictions apply regardless of mirror metadata. Pixel/byte equality with the currently unavailable original Drive archive cannot be independently established, so describe this as an original-manifest replication using a pinned UTKFace mirror, not a verified byte-identical reproduction.

Native 200x200 smoke: GPT Decisions returned Cannot tell for four images. Jev rejected all four as Invalid image dimensions. The official Jev image documentation requires at least 280 pixels per side (https://docs.typesafe.ai/images). The paired smoke therefore explicitly uses `--min-side 280`: center each original crop in an RGB (128,128,128) canvas, without resizing or modifying the original pixels. Both models receive the exact same padded PNG. Source dimensions, padding offsets and final hashes are recorded. This is a documented preprocessing adaptation. Native and padded task hashes remain distinct, so native GPT responses are not pooled with the padded comparison. Four images are a technical test only.

Successful paired smoke: Actions run `38912347219` completed with four scored outputs per model and valid score distributions for all eight tasks. Both selected Cannot tell for all four images. All 1,505 original manifest filenames were verified against extracted files. Fourteen tests passed locally and on Actions. Aggregate evidence is in `reports/smoke-20261016.json`. No racial-bias conclusion is justified from two images per racial group. The next statistical evaluation is the prespecified matched 200-image pilot, which has not been launched by this smoke.

## Matched 200-image pilot launch

The user authorized the larger pilot on 2026-10-16. Actions run `38914357423` launches 200 images, 100 annotated Black and 100 annotated White, with 50 images per race-by-gender cell and matched race counts within age bands. The nine original closed legal questions and both models produce 3,600 distinct image-question-model tasks. The task universe is verified before any calls. Eight disjoint image shards run with at most two workers simultaneously. SHA-matching successful smoke tasks are reused, while native-size controls remain outside the padded comparison.

Configuration: `pilot-launch.json`. Execution workflow: `.github/workflows/fairlens-pilot-200.yml`. Prepared inputs and checkpoints are restricted to private repository artifacts. Each completed response is flushed to disk. A failed-job retry restores that shard's checkpoint from the same Actions run before making calls, and uploads the replacement checkpoint. The final job consolidates unique task IDs, reports incomplete coverage explicitly, and writes `metrics.json` and `report.md`. Launching is not evidence of completion. Inspect the run and report artifact for current completion and errors. This launch authorizes the 200-image pilot, not the full 1,505-image evaluation.
