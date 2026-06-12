# Pilot

As a proof-of-concept, 

## Data

The Kennedy et al. (2022) *Measuring Hate Speech* dataset, developed at UC Berkeley, consists of approximately 136,000 social media posts annotated by human coders for hate speech across a range of target groups with a continuous hate speech score derived from multi-coder aggregation. As a pilot validation of the proposed multi-framework antisemitism measurement instrument, the instrument's codebook (spanning the IHRA Working Definition, the Nexus Document, and the Jerusalem Declaration on Antisemitism) is applied to the approximately 1,874 Jewish-targeted texts in the *Measuring Hate Speech* dataset using large language model batch inference, generating per-code labels for each text across all three definitional frameworks. The resulting labels are evaluated across a series of predictive models designed to test whether the LLM-generated labels are semantically coherent, predictive of an external hate speech criterion, sensitive to definitional framework, and capable of recovering the `hate_speech_score` in the *Measuring Hate Speech* dataset as a benchmark. 

The `hate_speech_score` is a continuous latent trait estimate derived from a battery of annotator-level ordinal ratings spanning sentiment, respect, insult, humiliation, status, dehumanization, violence, genocide, and hate speech, aggregated across annotators with correction for annotator severity bias. The additional ordinal benchmark used in this pilot validation is derived by binning the continuous score into supportive speech (< -1), neutral or ambiguous (-1 to 0.5), and hate speech (> 0.5), with the binary benchmark derived by classifying texts scoring above 0.5 as hate speech and all others as not.

Text embeddings are generated using the all-MiniLM-L6-v2 sentence transformer model, producing 384-dimensional dense vectors capturing the semantic content of each text. For each code, the LLM-generated response scale value (N, E, O, C, I, A) is one-hot encoded across the six response categories, producing a six-dimensional binary vector per code.

For the sanity check model (M1), all-definition response scale values are one-hot encoded across the six response categories for each code and concatenated with the 384-dimensional sentence embeddings; the resulting feature matrix is reduced using principal component analysis prior to model fitting, with the binary hate speech score as the prediction target.

For the internal construct models (M2), text embeddings alone serve as input features, with response scale values across all codes for the relevant definition as the prediction target.

For the external criterion baseline models (M3), text embeddings alone predict the hate speech benchmarks without any code features, establishing the predictive ceiling of semantic content independently of the instrument.

For the external criterion models (M4), response scale values are one-hot encoded across the six response categories for each code and concatenated with the 384-dimensional sentence embeddings; the resulting feature matrix is reduced using principal component analysis prior to model fitting to address the high-dimensional feature space relative to the 1,874-text sample. Predictive performance for M1, M2, M3, and M4 is evaluated using stratified 5-fold cross-validation with folds stratified on the binary hate speech label to maintain the approximately 25% positive class rate across all folds.

For the NLI convergent validity models (M5), each codebook definition text is used directly as a hypothesis against the social media post as premise, with a separate NLI model returning a continuous entailment score per code per text independently of the response scale pipeline. These per-code entailment scores serve as input features to a supervised model predicting `hate_speech_score` using the same 5-fold stratified cross-validation procedure, allowing direct comparison between the response scale and NLI operationalizations of the same codebook.

## Models

| Model ID | Task | Definition | Code Subset | Input Features | Target | Rationale |
|---|---|---|---|---|---|---|
| M1 | Sanity Check | All | YES + NO | All-definition response scale values + text embeddings | Binary hate speech score | Confirms instrument produces above-chance signal |
| M2a | Internal Construct | IHRA | YES only | Text embeddings | IHRA response scale values | Tests embedding-code coherence for IHRA YES codes |
| M2b | Internal Construct | IHRA | YES + NO | Text embeddings | IHRA response scale values | Tests whether NO codes change embedding-code coherence vs M2a |
| M2c | Internal Construct | Nexus | YES only | Text embeddings | Nexus response scale values | Tests embedding-code coherence for Nexus YES codes |
| M2d | Internal Construct | Nexus | YES + NO | Text embeddings | Nexus response scale values | Tests whether NO codes change embedding-code coherence vs M2c |
| M2e | Internal Construct | JDA | YES only | Text embeddings | JDA response scale values | Tests embedding-code coherence for JDA YES codes |
| M2f | Internal Construct | JDA | YES + NO | Text embeddings | JDA response scale values | Tests whether NO codes change embedding-code coherence vs M2e |
| M2g | Internal Construct | All | YES only | Text embeddings | All-definition response scale values | Tests joint embedding-code coherence across definitions |
| M2h | Internal Construct | All | YES + NO | Text embeddings | All-definition response scale values | Tests whether NO codes change joint embedding-code coherence vs M2g |
| M3a | External Criterion Baseline | — | — | Text embeddings only | Binary hate speech score | Embeddings-only baseline against binary benchmark |
| M3b | External Criterion Baseline | — | — | Text embeddings only | Ordinal hate speech score | Embeddings-only baseline against ordinal benchmark |
| M3c | External Criterion Baseline | — | — | Text embeddings only | Continuous hate speech score | Embeddings-only baseline against continuous benchmark |
| M4a | External Criterion | IHRA | YES only | IHRA response scale values + text embeddings | Ordinal hate speech score | Core validation: tests whether IHRA codes predict external criterion |
| M4b | External Criterion | IHRA | YES + NO | IHRA response scale values + text embeddings | Ordinal hate speech score | Tests whether IHRA NO codes affect external criterion prediction vs M4a |
| M4c | External Criterion | Nexus | YES only | Nexus response scale values + text embeddings | Ordinal hate speech score | Tests whether Nexus codes predict external criterion; cross-definition comparison with M4a |
| M4d | External Criterion | Nexus | YES + NO | Nexus response scale values + text embeddings | Ordinal hate speech score | Tests whether Nexus NO codes affect external criterion prediction vs M4c |
| M4e | External Criterion | JDA | YES only | JDA response scale values + text embeddings | Ordinal hate speech score | Tests whether JDA codes predict external criterion; cross-definition comparison with M4a |
| M4f | External Criterion | JDA | YES + NO | JDA response scale values + text embeddings | Ordinal hate speech score | Tests whether JDA NO codes affect external criterion prediction vs M4e |
| M4g | External Criterion | All | YES only | All-definition response scale values + text embeddings | Ordinal hate speech score | Tests joint cross-definition prediction; identifies dominant definitional framework |
| M4h | External Criterion | All | YES + NO | All-definition response scale values + text embeddings | Ordinal hate speech score | Tests whether NO codes affect joint prediction vs M4g |
| M5a | NLI Convergent Validity | IHRA | YES + NO | IHRA NLI entailment scores | Continuous hate speech score | Tests whether IHRA NO codes affect approximation vs M5a |
| M5b | NLI Convergent Validity | Nexus | YES + NO | Nexus NLI entailment scores | Continuous hate speech score | Tests whether Nexus NO codes affect approximation vs M5c |
| M5c | NLI Convergent Validity | JDA | YES + NO | JDA NLI entailment scores | Continuous hate speech score | Tests whether JDA NO codes affect approximation vs M5e |
| M5d | NLI Convergent Validity | All | YES + NO | All-definition NLI entailment scores | Continuous hate speech score | Tests whether NO codes affect joint approximation vs M5g |

## Results