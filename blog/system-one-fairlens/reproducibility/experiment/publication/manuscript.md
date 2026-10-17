# Refusals and language sensitivity in a FairLens replication with typed decision models

Scientific manuscript for author review | 16 October 2026

## Abstract

We evaluate two typed decision APIs on the complete closed question subset of FairLens, using its 1,505 official image entries, 38 questions and paired English and Brazilian Portuguese prompts. All 228,760 planned evaluations reached a terminal response. Jev served version 1.14.0 and GPT Decisions served gpt-6-luna. Their rankings depend on aggregation. English soundness is 83.12% versus 80.19% when every question has equal weight, but 75.94% versus 83.23% when each domain has equal weight. GPT produces 16,761 explicit refusals, concentrated in interview recommendations, while Jev produces none. The Portuguese condition changes performance in different directions across question groups. On the criminality question, Jev selects Criminal for 36 entries in English and seven in Portuguese. Its English Black minus White selection gap is 2.68 percentage points on independent, consistently annotated image inputs, with an unadjusted 95% interval of 0.27 to 5.66. The corresponding Portuguese interval includes zero. These are exploratory associations with model outputs. They establish neither actual criminality nor a causal effect of race. We provide raw responses, exact prompts, offline analyses and a translation review packet. Independent human validation of the Portuguese translation remains pending. The 31 open questions are outside the capabilities of these endpoints and were not evaluated.

## Introduction

An audit of judgments about people must distinguish a decision supported by a question, an admission that an image is insufficient, and a policy refusal. These outcomes can have different practical meanings while receiving the same benchmark score. This distinction becomes consequential when comparing a model that always returns a supplied category with one that often refuses.

FairLens [1] evaluates high stakes face judgments across hiring, legal and healthcare scenarios. Its closed questions measure whether answers follow stated evidence or recognize insufficient information. We replicate that closed subset with two decision APIs and add a paired Portuguese condition. Our contribution is a completed, inspectable replication and an analysis of how refusal handling, aggregation and this translation alter its interpretation. We do not propose a new fairness benchmark or identify an architectural cause for a difference between providers.

Related work already establishes the relevance of prompt and language variation. Wu et al. [2] audit vision language models on UTKFace and FACET using direct and choice prompts. Malik et al. [3] argue for multiple question formulations when evaluating demographic bias. Al Sahili et al. [4] document language dependent disparities in multilingual contrastive models. Our extension concerns typed decisions on the fixed FairLens split, with explicit accounting for refusals and paired output transitions.

<!-- pagebreak -->

## Methods

### Scope and data provenance

The executed inventory contains 38 closed questions, comprising 16 binary and 22 questions with more than two options. Hiring contributes 21, legal nine and healthcare eight. Each is evaluated for every official entry, model and language, giving 1,505 × 38 × 2 × 2 = 228,760 terminal evaluations. The 31 open questions were inventoried and translated but not executed. No free text judge score is reported.

We pin the upstream repository to commit 130205f243267fc90b973cb875d1711c2d932bbe. Official filenames and demographic metadata define the 1,505 entries. The original image archive was unavailable at acquisition, so we used a checksum pinned UTKFace cropped mirror. The manifest records its revision, archive hash and per image source and PNG hashes. Equality with the unavailable original archive cannot be independently established. Each 200 × 200 RGB crop is centered, without resizing, on a 280 × 280 neutral gray canvas to satisfy the image interface. Both models receive identical PNG bytes.

Five duplicate pairs reduce the cohort to 1,500 unique PNG inputs. Three unique inputs have conflicting demographic annotations. Descriptive tables retain all 1,505 official entries. Supplemental inference uses at most 1,497 unique inputs with consistent annotations, retaining the lexicographically first eligible entry. Dataset race, gender and age labels are analysis metadata. They and the filenames are not sent to either model.

### Endpoints and prompt construction

Jev requests jev-preview through /v1/systemone and records served model jev-1.14.0. GPT requests and records gpt-6-luna through /v1/decisions. Both receive a typed choice question with the supplied labels. The GPT adapter places the same prompt in both the user input and question instructions. The Jev adapter places it in question instructions. This difference is part of the executed protocol and precludes attributing provider differences solely to model architecture. Provider contracts define typed choices, probability vectors and refusal objects [5, 6]. We analyze returned choices rather than generating or parsing free text.

The English condition preserves the pinned question text and option order, with the domain context and closed answer suffix recorded in the manifest. The Portuguese condition translates the context, question, options and suffix together. Option mappings are one to one and inverted only after inference. Translation was authored and checked by AI. There is no independent human back translation or adjudication. Consequently, a paired difference measures these particular prompt packages, including wording and grammatical gender.

### Outcomes and statistical analysis

Benchmark soundness is the fraction matching the expected label. A refusal remains in the denominator and contributes zero matches. We additionally report category coverage and correctness conditional on a category response. These distinguish withheld decisions from incorrect labels. Cannot tell is a supplied category and is separate from an explicit API refusal. The benchmark expected labels are logical targets, not observations of a person's health, competence or conduct.

We report both equal question weighting and equal weighting of domain means. Original demographic parity and association programs are preserved with checksum provenance. Classifiable response analyses use explicitly labeled conditional denominators. Paired binary endpoints use exact two sided McNemar tests, with Holm adjustment across all 260 soundness, abstention, adverse choice and refusal tests. Percentile intervals use 2,000 image bootstrap resamples with seed 20261016. Black minus White selection differences use Newcombe intervals from Wilson intervals. Score differences and interactions are exploratory and unadjusted. Repeated questions do not create additional independent people. We conducted interim analyses, so adjustment does not turn the study into a preregistered confirmatory test.

<!-- pagebreak -->

## Overall results and refusal accounting

The run contains 211,999 category answers and 16,761 explicit refusals, with no unresolved task or HTTP failure in the consolidated terminal set. Jev returns a category on every task. GPT refuses 8,242 of 57,190 English tasks and 8,519 of 57,190 Portuguese tasks. These are 14.41% and 14.90% respectively. Historical errors and retries exist in checkpoints and are not counted as extra experimental observations.

| Condition | Hiring | Legal | Healthcare | All questions | Equal domains |
|---|---:|---:|---:|---:|---:|
| Jev EN | 97.75 | 65.32 | 64.74 | 83.12 | 75.94 |
| Jev PT | 90.03 | 75.59 | 63.97 | 81.12 | 76.53 |
| GPT EN | 74.08 | 86.57 | 89.04 | 80.19 | 83.23 |
| GPT PT | 73.06 | 85.12 | 90.37 | 79.56 | 82.85 |

Table 1. Soundness percentages with all terminal responses in the denominator. Domain totals per condition are 31,605 for hiring, 13,545 for legal and 12,040 for healthcare. The last two columns apply different weights to these same responses.

Hiring contains 21 of 38 questions, so equal question weighting gives it 55.26% of the overall score. Equal domain weighting gives it one third. Jev's advantage in hiring and GPT's advantage in legal and healthcare therefore produce the ranking reversal in Table 1. Neither summary supports a uniform ordering across the benchmark.

![Sound and incorrect category responses and explicit refusals by domain](figures/domain-outcomes.png)

Figure 1. Every bar accounts for all assigned tasks. Refusal is an observed API outcome. It is counted as a nonmatch by the benchmark, while remaining separate from an incorrect category in this figure.

On healthcare items tagged for demographic association, Jev assigns a nonneutral category in 28.36% of English and 26.94% of Portuguese category responses. GPT rates are 11.96% and 10.98%. The supplement includes every original parity and association report and an explicit domain summary. Refusal markers remain unparsed in the original association program, within its denominator but outside both neutral and nonneutral counts. A low adverse rate or small parity gap must therefore be interpreted alongside unsupported labels and refusals.

FairLens reports English equal domain soundness of 93.8% for Ovis2.5, 88.1% for InternVL3, 85.7% for Qwen2.5-VL and 77.1% for GPT-5.2-reasoning [1]. Our Jev and GPT results are 75.94% and 83.23%. This is an aggregate contextual comparison, not a paired significance test against those systems. We have not rerun them through the present adapters. Different decoding, interfaces and image acquisition limit a shared leaderboard interpretation.

<!-- pagebreak -->

## Question groups and paired translation results

All eight question groups are complete. Figure 2 shows substantial variation within hiring and healthcare. The groups organize related tasks for interpretation and execution. They are not eight independent datasets.

![Soundness across eight question groups and four conditions](figures/group-soundness.png)

Figure 2. Percent matching the expected category, including refusals in each denominator. Every question uses all 1,505 official entries. EN denotes English and PT Brazilian Portuguese.

Interview recommendations explain most GPT refusals. Across the six questions, 8,180 of 9,030 English tasks and 8,515 of 9,030 Portuguese tasks are refused. The remaining 850 and 515 category responses all match the benchmark. Thus benchmark soundness of 9.41% and 5.70% coexists with 100% conditional correctness and low category coverage. Only 70 of the 9,030 official entry question pairs have category responses in both languages. A comparison restricted to that selected subset cannot characterize all interview decisions. The paired refusal analysis retains refusals and is provided alongside it.

Jev's trust related hiring group falls from 97.81% in English to 48.90% in Portuguese, while its legal domain rises from 65.32% to 75.59%. The direction is therefore question dependent. On the healthcare doctor trust question, Jev selects the benchmark expected Yes for 248 English entries and five Portuguese entries. These differences should trigger a semantic audit of the executed prompts. They do not establish a general Portuguese effect.

Across the complete family of paired tests, Jev has 21 soundness comparisons with Holm adjusted p < .05, of which ten favor Portuguese and 11 favor English. GPT has four, with one favoring Portuguese and three favoring English, conditional on responses classifiable in both languages. The supplement retains every test, its paired sample size and marginal interval. Correlated and sometimes identical endpoints remain in the declared adjustment family. Reporting these counts does not make the question set representative of all possible prompt formulations.

<!-- pagebreak -->

## Exploratory criminality analysis

The legal criminality item is legal-07. It supplies Criminal, Law-abiding Civilian and Cannot tell. Jev chooses Criminal for 36 of 1,505 English entries, Law-abiding Civilian for 425 and Cannot tell for 1,044. Portuguese counts are seven, 90 and 1,408 respectively. Inferring the favorable category from appearance is also unsupported. Counting only Criminal would overlook most failures to recognize insufficient evidence.

| Condition | Criminal among Black entries | Criminal among White entries | Cannot tell overall | Refusals |
|---|---:|---:|---:|---:|
| Jev EN | 18 / 353 | 15 / 622 | 1,044 / 1,505 | 0 |
| Jev PT | 1 / 353 | 6 / 622 | 1,408 / 1,505 | 0 |
| GPT EN | 0 / 352 | 0 / 622 | 1,504 / 1,505 | 1 |
| GPT PT | 0 / 353 | 0 / 622 | 1,505 / 1,505 | 0 |

Table 2. Original entry counts. The English GPT refusal is a Black annotated entry and is excluded only from the category denominator in columns two and three. Inferential intervals below use unique inputs with consistent demographic annotations, so their denominators differ.

On independent, consistently annotated images, Jev's English Black minus White Criminal selection difference is 2.68 percentage points, with an unadjusted 95% Newcombe interval of 0.27 to 5.66. The Portuguese estimate is −0.69 points, with an interval of −1.85 to 0.72. GPT has no Criminal selections in either language. Its English difference is zero with a 95% interval of approximately −0.62 to 1.08 points, illustrating why zero observed events do not establish zero population disparity.

For Jev, paired Portuguese minus English Criminal selection changes by −1.94 percentage points on 1,497 inputs, with a 95% bootstrap interval of −2.67 to −1.27. There are 29 downward and zero upward transitions, with exact McNemar p = 3.73 × 10⁻⁹ and Holm adjusted p = 8.05 × 10⁻⁷. Cannot tell increases by 24.18 points, with an interval of 21.98 to 26.39. These within image results concern the complete translated prompt package.

Choices and score vectors tell different stories. Jev's mean Criminal score increases by 1.07 points in Portuguese, with an unadjusted interval of 0.82 to 1.31, even as Criminal selections decrease. More score mass can shift into Criminal while Cannot tell still wins more decisions. The English Black minus White mean score gap is 2.05 points, with an interval of 0.47 to 3.68. The Portuguese gap is 0.04 points, with an interval of −1.10 to 1.16. These are API category scores. They are not calibrated probabilities of real criminality, and scores are not necessarily calibrated comparably between providers.

The contract audit identifies an additional precision limitation. All returned category probabilities in both APIs have at most two decimal places. Of 114,380 Jev category responses, 612 vectors differ from a sum of one, by at most 0.01. In 11 cases the selected label has a displayed probability 0.01 below the displayed maximum. The supplement preserves all examples. We retain the returned choice and scores without renormalization or replacement. Rounding or internal decision precision is a possible explanation, but is not verified by these responses. Neither discrepancy occurs in GPT responses. API score precision limits interpretations of very small score differences.

We highlight this question because it motivated the audit, but detailed contrasts and interactions were examined after preliminary results. Race annotations correlate with other properties of these images. There is no randomized race intervention, controlled counterfactual image construction or adjustment sufficient to identify a causal race effect. A disparity in outputs warrants scrutiny without implying a criminality label for any depicted person.

<!-- pagebreak -->

## Discussion and limitations

The strongest methodological finding is that an aggregate score can obscure the kind of decision a system makes. A policy refusal and an unsupported adverse label are both nonmatches under soundness, but have different consequences. Conversely, treating every refusal as sound would hide a system's failure to follow a hypothetical question that supplies sufficient qualifications. We therefore retain the benchmark definition and report the full outcome decomposition. Coverage and correctness among category responses must be read together because the classifiable subset is selected by the model.

Aggregation also affects the apparent overall winner. Our question weighted and domain weighted scores are both exactly reproducible, but answer different questions. A headline comparison should specify its weights and show the underlying domain values. The complete group and question tables prevent the aggregate from standing in for a uniform safety claim.

The Portuguese evaluation adds evidence of prompt sensitivity, while leaving its mechanism unresolved. It changes instructions, scenario wording, grammatical gender and category labels together. The translated version has not received independent human review, and structural bijection does not prove semantic equivalence. The supplied review packet covers all 69 source questions, both sets of context instructions and both answer suffixes. Any corrections must produce a new translation version. They cannot retroactively validate the executed prompts. A fresh, separately budgeted experiment would be needed to evaluate revised wording.

Other limitations constrain external interpretation. We use one fixed public benchmark cohort, one translated formulation per question and one recorded terminal response per assigned task. Transport retries are operational recovery, not independent repetitions. Stochastic or temporal variation is not estimated, and aliases and vendor policies may evolve. The provider adapters differ and we cannot separate architecture, training, safety policy or prompt placement as causes. Public benchmark exposure in training is unknown. The unavailable original archive limits byte level replication despite filename matching and recorded source hashes.

Dataset demographic categories are inherited annotations rather than self identified demographic facts. Their binary gender scheme, heterogeneous Other category and unequal group sizes limit generalization. Duplicate photographs and conflicting annotations are disclosed and removed from supplemental inference. Exact PNG deduplication cannot establish that every remaining photograph depicts a different person, so residual identity dependence is possible. The bootstrap describes variation across available unique inputs, not repeated model runs or a representative population sample. Small intersectional cells are not used to support broad claims. Unadjusted subgroup and score intervals remain exploratory. A degenerate percentile interval at zero observed changes is accompanied by marginal Wilson intervals and should not be read as certainty.

The original study's per response model outputs were not available in the inspected public resources. Its reported aggregates provide context, but not the paired observations required for direct uncertainty estimates against those models. The present study also omits all free text questions and cannot assess appearance based reasoning in generated explanations. A complete replication of every FairLens component would require a different endpoint capability and a separate protocol.

These results support a replication and audit paper, with its contribution concentrated in transparent output accounting and bilingual sensitivity. They do not establish that all typed decision systems are safer or less safe than generative models. Independent translation review and author confirmation of disclosures remain necessary before a submission is presented as ready.

<!-- pagebreak -->

## Reproducibility and responsible use

The review package contains one lossless JSONL record per completed task, normalized observations, image and prompt hashes, all executed question variants, reconstructed request templates, complete metrics and all 260 paired tests. Raw response bodies are preserved. No credentials, authorization headers or image bytes are included. Request templates are reconstructed from the executed adapter and manifest, rather than represented as separately logged wire payloads. Image acquisition requires the relevant dataset access and terms.

The offline verifier checks package hashes, task identity, normalization fidelity, coverage, probability vectors, domain counts and paired test statistics. The original three metric programs and their configuration are preserved under their source provenance. Analyses can be reproduced without paid inference. Repeating model inference is a distinct operation and may not reproduce hosted model behavior exactly.

The source cohort contains photographs of real people. Dataset access does not establish individual consent for sensitive judgments, and the original noncommercial research restriction remains relevant. We analyze output patterns without treating model assigned traits as truths about people. The prepared supplement is for author review. Public distribution has not been performed, and any public package must retain dataset conditions, upstream attribution and applicable rights. No mitigation or causal intervention is claimed.

AI assistance was used for code, analysis, translation and manuscript drafting. Independent human translation review is pending. Authorship, affiliations, funding, conflicts, the appropriate institutional review statement and final approval of all claims must be supplied or confirmed by the human authors before submission. No institutional approval, consent or peer review is claimed here.

## References

[1] Vahid Reza Khazaie, Ahmed Y. Radwan and Shaina Raza. 2026. FairLens Benchmarking Fairness in Vision Language Models for High Stakes Decision Making. arXiv:2609.01691v1. https://arxiv.org/abs/2609.01691

[2] Xuyang Wu, Yuan Wang, Hsin-Tai Wu, Zhiqiang Tao and Yi Fang. 2025. Evaluating Fairness in Large Vision-Language Models Across Diverse Demographic Attributes and Prompts. Findings of EMNLP, 22973–22991. https://doi.org/10.18653/v1/2025.findings-emnlp.1251

[3] Shaivi Malik, Hasnat Md Abdullah, Sriparna Saha and Amit Sheth. 2026. Ask Me Again Differently GRAS for Measuring Bias in Vision Language Models on Gender Race Age and Skin Tone. Findings of EACL, 2327–2388. https://doi.org/10.18653/v1/2026.findings-eacl.123

[4] Zahraa Al Sahili, Ioannis Patras and Matthew Purver. 2025. Breaking Language Barriers or Reinforcing Bias A Study of Gender and Racial Disparities in Multilingual Contrastive Vision Language Models. IJCNLP AACL, 331–352. https://doi.org/10.18653/v1/2025.ijcnlp-long.20

[5] TypeSafe AI. System One API documentation. Choice question contract. Accessed 16 October 2026. https://docs.typesafe.ai/api

[6] OpenAI. Decisions API documentation. Typed choices and explicit refusals. Accessed 16 October 2026. https://developers.openai.com/api/docs/guides/decisions

[7] Vector Institute. FairLens source and question configuration. Commit 130205f243267fc90b973cb875d1711c2d932bbe. https://github.com/VectorInstitute/fairlens
