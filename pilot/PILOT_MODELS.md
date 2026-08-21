# `models.ipynb` Cell Map

## Table of Contents
- [Setup](#setup): loads every base file (targets, folds, embeddings, code features, NLI scores) and defines every shared helper function used by every later section
- [Create Features](#create-features): builds the base files Setup loads, one-hot encodes LLM labels, creates the stratified fold split, embeds all comment text
- [PCA by Fold](#pca-by-fold): reduces the sentence embeddings to fewer components, fit separately per fold to avoid leakage
- [Load Targets](#load-targets): builds the continuous, ordinal, and binary target variables every model predicts
- [Data Shape (EDA)](#data-shape-eda): exploratory diagnostics on the corpus and labels, distributions, overlap, term extraction, topic mapping
- [Sanity Check](#sanity-check): first-pass binary classification test confirming the features carry real signal before the full ablation grid
- [Embedding Only](#embedding-only): tests text embeddings alone as predictors of the continuous, ordinal, and binary targets, the baseline every other feature combination is compared against
- [Internal Construct](#internal-construct): tests whether the LLM's own code labels can be recovered from embeddings alone
- [Label Collinearity Check](#label-collinearity-check): diagnoses multicollinearity among code features, including the batching-contamination test
- [Codes Only](#codes-only): LLM-derived code features alone predicting the ordinal target
- [Codes and Embeddings](#codes-and-embeddings): combines codes with embeddings to test complementarity
- [NLI Analysis](#nli-analysis): full ablation using NLI v1 entailment scores plus the first LLM-vs-NLI relationship and disagreement diagnostics
- [V2 NLI Zero-shot](#v2-nli-zero-shot): repeats the NLI ablation and diagnostics using the larger v2 DeBERTa model
- [NLI Meta-Analysis](#meta-analysis): cross-version diagnostics comparing v1 and v2, including the per-code disagreement check that revealed several codes had ungrammatical or malformed hypothesis text
- [NLI Hypothesis Prefix](#hypothesis-prefix): reruns the ablation and diagnostics using the corrected hypothesis versions, plus cross-variant comparisons
- [Rerankers](#rerankers): tests bge and qwen relevance scores as an alternative to NLI, including the full six-source ablation and synergy scan

---

## Analysis and Ablation Overview

Every analysis and ablation stage in the notebook, in order of appearance, with the feature sets, target(s), and models compared in each.

| Stage | Feature Set(s) | Target(s) | Models/Methods Compared | Cells |
|---|---|---|---|---|
| Sanity check | Code scale (YES+NO) + PCA embeddings, all definitions | Binary | XGBoost (grid search, SHAP), Logistic Regression | [17](#cell-17), [18](#cell-18) |
| Embeddings baseline | PCA vs. raw embeddings | Binary, Ordinal, Continuous | LogReg vs. XGBoost (binary); Ordinal Logit, Multinomial, OvR, OvO, XGBoost-threshold (ordinal); Ridge vs. XGBoost Regressor (continuous) | [21](#cell-21), [22](#cell-22), [23](#cell-23) |
| Internal construct validity | Embeddings only, per definition and code subset (yes-only vs. yes-and-no) | LLM's own code labels (E/I/A) | Logistic Regression, MultiOutputClassifier, XGBoost | [25](#cell-25), [26](#cell-26), [27](#cell-27), [28](#cell-28), [29](#cell-29) |
| Label collinearity check | Code features (YES vs. NO pairs) | n/a (diagnostic, not predictive) | Correlation matrix, within-block vs. across-block significance test | [31](#cell-31), [32](#cell-32), [33](#cell-33), [34](#cell-34) |
| Codes only | Code scale, per definition and code subset | Ordinal | Ordinal Logit, Multinomial, OvR, OvO, XGBoost-threshold; multinomial coefficient extraction; permutation control | [37](#cell-37), [38](#cell-38), [39](#cell-39) |
| Codes and embeddings | Code scale + PCA/raw embeddings, per definition and code subset | Ordinal | Same ordinal model set as Codes Only | [41](#cell-41) |
| NLI ablation, v1 | NLI (v1) alone, plus embeddings, plus codes, plus codes+embeddings, all definitions | Continuous, Ordinal, Binary | Ridge, Ordinal Logit, Multinomial, OvR, OvO, Logistic Regression | [43](#cell-43) |
| LLM label vs. NLI relationship, v1 | NLI (v1) entailment score vs. LLM ordinal label | n/a (diagnostic) | OLS, Spearman correlation, high-entailment proportion by label | [44](#cell-44) |
| LLM vs. NLI disagreement, v1 | Pooled LLM labels and NLI (v1) scores | n/a (diagnostic) | Type 1/Type 2 disagreement flagging | [46](#cell-46) |
| NLI ablation, v2 | Same structure as v1 ablation, NLI (v2) | Continuous, Ordinal, Binary | Same model set as v1 ablation | [48](#cell-48) |
| LLM label vs. NLI relationship, v2 | NLI (v2) entailment score vs. LLM ordinal label | n/a (diagnostic) | Same as v1 relationship diagnostic | [49](#cell-49) |
| LLM vs. NLI disagreement, v2 | Pooled LLM labels and NLI (v2) scores | n/a (diagnostic) | Same as v1 disagreement analysis | [50](#cell-50) |
| Multicollinearity, v1 vs. v2 | NLI (v1, v2) entailment scores, codes, raw embeddings | n/a (diagnostic) | Fast VIF via correlation matrix inversion | [52](#cell-52) |
| Per-code disagreement, v1 and v2 | LLM label vs. NLI entailment, per code | n/a (diagnostic) | Spearman correlation per code, hypothesis text inspection | [53](#cell-53), [54](#cell-54), [55](#cell-55) |
| NLI ablation, hypothesis-fixed | NLI (v1_prefix, v2_prefix) alone, plus embeddings, plus codes, plus codes+embeddings | Continuous, Ordinal, Binary | Same model set as earlier NLI ablations | [57](#cell-57) |
| LLM label vs. NLI relationship, hypothesis-fixed | NLI (v1_prefix, v2_prefix) entailment vs. LLM ordinal label | n/a (diagnostic) | Same as earlier relationship diagnostics | [58](#cell-58) |
| Largest disagreements, four NLI variants | v1, v2, v1_prefix, v2_prefix entailment scores vs. LLM label and Kennedy score | n/a (diagnostic) | Side-by-side disagreement ranking | [59](#cell-59) |
| Feature importance, four NLI variants | NLI plus codes (All), each of the four NLI variants | Continuous | Ridge coefficient extraction | [60](#cell-60) |
| Residual overlap, four NLI variants | v1, v1_prefix, v2, v2_prefix predictions | Continuous | Per-comment residual comparison across variants | [61](#cell-61) |
| Reranker score distributions | bge, qwen relevance scores (raw and recovered logit) | n/a (diagnostic) | Per-code distribution summary | [63](#cell-63) |
| Full ablation, six sources | v1, v2, v1_prefix, v2_prefix, qwen, bge, alone and combined, all definitions | Continuous, Ordinal, Binary | Same model set as earlier NLI ablations, selective feature scaling | [64](#cell-64), [65](#cell-65) |
| Pairwise synergy scan | Every single source and pair among codes, v1, v2, v1_prefix, v2_prefix, qwen, bge, raw, pca | Continuous | Ridge, absolute performance and synergy-over-best-single comparison | [66](#cell-66) |
| LLM label vs. reranker relationship | bge, qwen relevance score (logit) vs. LLM ordinal label | n/a (diagnostic) | OLS, Spearman correlation, high-relevance proportion by label | [67](#cell-67) |

---

## Setup

<a id="cell-1"></a>`Cell 1 (code)`: Master setup cell: loads targets/folds, defines `ordinal_bin`, builds fold-getter helpers, loads embeddings and PCA/raw feature-loaders, sets `LOGREG_C`/`XGB_PARAMS`, loads and filters code features by `MIN_SUPPORT`, builds `code_block_map`/`definition_prefix_map`, defines `get_code_columns` and `code_cols_for_definition`, loads NLI scores and pivots to wide format. Everything downstream depends on this cell.

---

## Create Features

<a id="cell-3"></a>`Cell 3 (code)`: Builds the full feature/target pipeline from raw sources: one-hot encodes LLM labels into `code_features.csv`, creates stratified 5-fold assignment by ordinal bin, embeds all comment text via `all-MiniLM-L6-v2` into `embeddings.csv`, saves `targets_and_folds.csv`. This is the cell that generates the base files `Cell 1` later loads.

---

## PCA by Fold

<a id="cell-5"></a>`Cell 5 (code)`: Selects PCA component count via scree analysis (90% variance threshold), fits/transforms PCA separately per fold (leakage-safe), saves per-fold train/test PCA CSVs to `features/pca/`.

---

## Load Targets

<a id="cell-7"></a>`Cell 7 (code)`: Builds three separate target Series from `judaism`: continuous (`hate_speech_score`), ordinal (mapped supportive/neutral/hate to 0/1/2), and binary (`>0.5` threshold).

---

## Data Shape (EDA)

<a id="cell-9"></a>`Cell 9 (code)`: Label distribution table by code and label source (GPT-4o vs. Sonnet), plus overall corpus/label summary stats.

<a id="cell-10"></a>`Cell 10 (code)`: Comment length distribution (word count, character count), histogram plot saved to `viz/`.

<a id="cell-11"></a>`Cell 11 (code)`: Cross-definitional flagging overlap check: does a comment flagged under one framework (IHRA/Nexus/JDA) tend to also be flagged under the others; pairwise agreement/disagreement counts.

<a id="cell-12"></a>`Cell 12 (code)`: Concept-map-based overlap: counts how many codes across IHRA/Nexus/JDA map to the same underlying concept (using a manually built `concept_map`).

<a id="cell-13"></a>`Cell 13 (code)`: c-TF-IDF computation per code, prints top-15 highest-weighted terms per code.

<a id="cell-14"></a>`Cell 14 (code)`: Interactive intertopic distance map: 2D UMAP/PCA projection of each code's c-TF-IDF vector, bubble size equal to comment count, colored by definition, saved as interactive HTML.

<a id="cell-15"></a>`Cell 15 (code)`: KDE comparison plot of `hate_speech_score` distribution, full Measuring Hate Speech corpus vs. the Jewish-targeted pilot subset, with supportive/neutral/hate threshold lines.

---

## Sanity Check

<a id="cell-17"></a>`Cell 17 (code)`: Sanity-check binary classification stage using XGBoost: all definitions, YES+NO codes, code-scale plus PCA embeddings, predicting binary target. Includes grid search, SHAP importance, per-fold ROC tracking.

<a id="cell-18"></a>`Cell 18 (code)`: Same sanity-check stage as Cell 17, but with Logistic Regression instead of XGBoost.

---

## Embedding Only

<a id="cell-20"></a>`Cell 20 (code)`: Shared feature-builder setup (PCA vs. raw embeddings) reused across the three target types in this section.

<a id="cell-21"></a>`Cell 21 (code)`: Embeddings-only baseline, binary target: PCA vs. raw embeddings, Logistic Regression vs. XGBoost.

<a id="cell-22"></a>`Cell 22 (code)`: Embeddings-only baseline, ordinal target: PCA vs. raw embeddings, comparing ordinal logit, multinomial, OvR, OvO, and XGBoost (regression-threshold).

<a id="cell-23"></a>`Cell 23 (code)`: Embeddings-only baseline, continuous target: PCA vs. raw embeddings, tuned Ridge vs. XGBoost Regressor.

---

## Internal Construct

<a id="cell-25"></a>`Cell 25 (code)`: Internal construct validity stage: defines the function to predict the model's own LLM code labels (E/I/A) from embeddings alone, per definition and code subset (yes-only vs. yes-and-no).

<a id="cell-26"></a>`Cell 26 (code)`: Runs the Cell 25 function across all definitions (IHRA/Nexus/JDA/All) and both code subsets, concatenates results, prints summary.

<a id="cell-27"></a>`Cell 27 (code)`: In-depth breakdown of the internal construct results (column inspection, fold counts, further stats).

<a id="cell-28"></a>`Cell 28 (code)`: Internal construct validity broken down per individual response class (E/I/A separately, not pooled).

<a id="cell-29"></a>`Cell 29 (code)`: Aggregates the per-class breakdown from Cell 28 by individual code and response level, prints summary table.

---

## Label Collinearity Check

<a id="cell-31"></a>`Cell 31 (code)`: Correlation check between `n_codes_evaluated` and `macro_auc`, within each definition times model group.

<a id="cell-32"></a>`Cell 32 (code)`: Correlation matrix restricted to YES-vs-NO code pairs within the same definition; flags high-magnitude correlation pairs as a quick multicollinearity check.

<a id="cell-33"></a>`Cell 33 (code)`: Isolates YES-vs-NO code correlations using the actual LLM batch/block assignment, not just definition.

<a id="cell-34"></a>`Cell 34 (code)`: Statistical test: are within-block code pairs more correlated than across-block pairs (the batching-contamination diagnostic).

<a id="cell-35"></a>`Cell 35 (code)`: Defines `concept_map` (manual grouping of codes across IHRA/Nexus/JDA into shared underlying concepts, e.g. "Collective blame"), used by Cells 11 and 12 and elsewhere.

---

## Codes Only

<a id="cell-37"></a>`Cell 37 (code)`: Code-features-only (no embeddings) ablation for the ordinal target, per definition and code subset.

<a id="cell-38"></a>`Cell 38 (code)`: Extracts per-class coefficients from the multinomial logistic model, per code, across folds (feature importance/interpretation).

<a id="cell-39"></a>`Cell 39 (code)`: Permutation control test: shuffles code labels, reruns the same model, checks whether performance collapses (validity check on the codes-only signal).

---

## Codes and Embeddings

<a id="cell-41"></a>`Cell 41 (code)`: Code features plus embeddings (PCA vs. raw) combined ablation for the ordinal target, per definition and code subset.

---

## NLI Analysis

<a id="cell-42"></a>`Cell 42 (markdown)`: Notes that NLI scoring itself happens in the separate `nli.ipynb` (Colab).

<a id="cell-43"></a>`Cell 43 (code)`: Full NLI ablation (v1): NLI alone, NLI plus embeddings, NLI plus codes, NLI plus codes plus embeddings, across all definitions and all three target types (continuous/ordinal/binary), ordinal comparing OvR/OvO/multinomial/ordinal-logit.

<a id="cell-44"></a>`Cell 44 (code)`: Relationship diagnostic (v1): LLM ordinal label vs. NLI entailment score, comparative full codebook vs. MIN_SUPPORT-filtered codebook (OLS/Spearman/high-entailment breakdown).

<a id="cell-45"></a>`Cell 45 (code)`: Parses the original `config.py` codebook blocks (`I_1` through `J_NO_1`) into the `codebook` dict via regex (the original, pre-fix hypothesis parser).

<a id="cell-46"></a>`Cell 46 (code)`: LLM-vs-NLI (v1) disagreement analysis: builds pooled ordinal labels, flags Type 1/Type 2 disagreement cases.

### V2 NLI Zero-shot

<a id="cell-48"></a>`Cell 48 (code)`: Same full NLI ablation structure as Cell 43, run for v2 (DeBERTa-v3-large) instead of v1.

<a id="cell-49"></a>`Cell 49 (code)`: Same relationship diagnostic as Cell 44, run for v2.

<a id="cell-50"></a>`Cell 50 (code)`: LLM-vs-NLI (v2) disagreement analysis, same structure as Cell 46.

### Meta-Analysis

<a id="cell-52"></a>`Cell 52 (code)`: Multicollinearity check comparing v1 vs. v2 entailment scores against codes and raw embeddings, using the fast VIF-via-correlation-matrix-inversion method.

<a id="cell-53"></a>`Cell 53 (code)`: Per-code disagreement between LLM label and NLI entailment score, v1 and v2 side by side; flags codes where entailment doesn't track the LLM's own label and prints the actual hypothesis text used (the diagnostic that surfaced the E13/carve-out hypothesis bugs).

<a id="cell-54"></a>`Cell 54 (code)`: Support-count check (label value counts) restricted to the `consistent_failures` codes flagged by Cell 53.

<a id="cell-55"></a>`Cell 55 (code)`: Full text printout for the E12/E13 criminal-act code cluster: every non-N LLM label, and every LLM/NLI disagreement case, v1 and v2, with actual comment text.

### Hypothesis Prefix

<a id="cell-57"></a>`Cell 57 (code)`: Full NLI ablation (same structure as Cell 43/48) run for both `v1_prefix` and `v2_prefix` (the hypothesis-fix versions), per fold.

<a id="cell-58"></a>`Cell 58 (code)`: Same relationship diagnostic as Cell 44/49, run comparatively for `v1_prefix` and `v2_prefix`.

<a id="cell-59"></a>`Cell 59 (code)`: Prints the largest LLM-vs-NLI disagreements across all four NLI variants (v1/v2/v1_prefix/v2_prefix) side by side, alongside the Kennedy continuous and ordinal target values for the same comments.

<a id="cell-60"></a>`Cell 60 (code)`: Ridge coefficient feature-importance printout for `nli_plus_codes_All`, across all four NLI variants.

<a id="cell-61"></a>`Cell 61 (code)`: Per-comment residual overlap analysis: checks whether v1/v1_prefix/v2/v2_prefix miss on the same comments (shared blind spot) or different ones (genuine complementarity), plus a breakdown of which codes are flagged within each hard-comment group.

### Rerankers

<a id="cell-63"></a>`Cell 63 (code)`: Loads reranker score files (bge, qwen), computes and appends the recovered raw logit column (`sigmoid_to_logit`) if not already present, prints per-code score distributions.

<a id="cell-64"></a>`Cell 64 (code)`: Full ablation across all six sources (v1, v2, v1_prefix, v2_prefix, qwen, bge), per fold, parallelized via `joblib`, with selective feature scaling (logits/embeddings scaled, codes/entailment scores not).

<a id="cell-65"></a>`Cell 65 (code)`: Summary table: best/worst `feature_set` per target type, and best/worst ordinal model overall, from the Cell 64 results.

<a id="cell-66"></a>`Cell 66 (code)`: Pairwise synergy scan: every single source and every pair (excluding invalid v1+v1_prefix and v2+v2_prefix combinations), definition="All" only, parallelized; reports absolute performance (`r2_pair`) and synergy gain over the best individual source.

<a id="cell-67"></a>`Cell 67 (code)`: Relationship diagnostic (reranker version of Cell 44/49/58): LLM ordinal label vs. reranker relevance score (logit), comparative full codebook vs. MIN_SUPPORT-filtered codebook, for both bge and qwen, with minty-green ECDF/violin plots.