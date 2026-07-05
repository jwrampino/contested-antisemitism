# Pilot

## Data

The *Measuring Hate Speech* dataset, developed at UC Berkeley, consists of approximately 136,000 social media posts annotated by human coders for hate speech across a range of target groups with a continuous hate speech score derived from multi-coder aggregation. As a pilot validation of the proposed multi-definitional construct, data labeled using the codebook is applied to the approximately 1,874 Jewish-targeted texts in the *Measuring Hate Speech* dataset using large language model batch inference, generating code-level labels for each text across all three definitional frameworks. The LLM-generated labels are benchmarked on whether they are capable of recovering the `hate_speech_score` variable in the *Measuring Hate Speech* dataset.

The dataset's `hate_speech_score` is a continuous estimate derived from annotator-level ordinal ratings across sentiment, respect, insult, humiliation, status, dehumanization, violence, genocide, and hate speech, aggregated across annotators with correction for annotator severity bias. The ordinal benchmark is derived by binning the continuous score into supportive speech (< -1), neutral or ambiguous (-1 to 0.5), and hate speech (> 0.5), based on the dataset's reported approximate thresholds. A hate speech binary is then derived further by classifying texts scoring above 0.5 as hate speech, and all others as not.

Text embeddings are generated using the all-MiniLM-L6-v2 sentence transformer model, producing 384-dimensional dense vectors capturing the semantic content of each text. For each code, the LLM-generated response scale value (N, E, I, A) is one-hot encoded across E, I, and A, dropping N as the reference category, producing a three-dimensional binary vector per code. All supervised models use stratified 5-fold cross-validation with folds stratified on the binary hate speech label to maintain the approximately 25% positive class rate across all folds. Where text embeddings are used alongside code features, (dimensionality reduction!!!!!!) is applied to the combined feature matrix within each training fold 

 project onto the held-out fold to prevent leakage.



## Models

The pilot uses a hierarchical block ablation design to evaluate the incremental and convergent validity of the instrument across separate and joint definitions in which each stage adds or substitutes a feature set.

**Sanity check.** All-definition response scale values (one-hot encoded, N dropped) concatenated with text embeddings, predicting the binary hate speech score. Confirms the instrument produces above-chance signal before any further decomposition.

**Embeddings baseline.** Text embeddings alone predict the binary, ordinal, and continuous hate speech benchmarks without any code features. Establishes the predictive ceiling of semantic content independently of the instrument, serving as the baseline against which all code-based stages are compared.

**Internal construct validity.** Text embeddings predict response scale values for each definition (YES codes only, then YES and NO codes together) and jointly across all three definitions. Tests whether the semantic content of a text is coherent with its instrument labels, and whether including NO codes changes that coherence. A low predictive relationship between embeddings and labels would indicate the instrument captures structured features beyond raw semantic content.

**Codes only.** Response scale values alone (no text embeddings) predict the ordinal hate speech score, evaluated separately for each definition (YES only, then YES and NO) and jointly. Tests whether the structured label output of the instrument independently predicts an external criterion without any access to the underlying text, the strongest standalone validity test for the codebook.

**Codes and embeddings.** Response scale values concatenated with text embeddings predict the ordinal hate speech score, evaluated separately for each definition (YES only, then YES and NO) and jointly. The incremental gain over the embeddings baseline quantifies the contribution of the instrument labels beyond semantic content, and the incremental gain over codes only quantifies the contribution of semantic content beyond the instrument labels.

**NLI convergent validity.** Each codebook definition text is used directly as a hypothesis against the social media post as premise, with an NLI model returning a continuous entailment score per code per text independently of the response scale pipeline. These per-code entailment scores predict the continuous `hate_speech_score`, evaluated separately for each definition and jointly. Convergence between the NLI operationalization and the response scale operationalization on the same codebook, derived through methodologically independent processes, constitutes convergent validity evidence.

| Stage | Definition | Code Subset | Input Features | Target |
|---|---|---|---|---|
| Sanity check | All | YES + NO | Response scale values + embeddings | Binary |
| Embeddings baseline | — | — | Embeddings only | Binary, ordinal, continuous |
| Internal construct | IHRA | YES only | Embeddings | IHRA response scale values |
| Internal construct | IHRA | YES + NO | Embeddings | IHRA response scale values |
| Internal construct | Nexus | YES only | Embeddings | Nexus response scale values |
| Internal construct | Nexus | YES + NO | Embeddings | Nexus response scale values |
| Internal construct | JDA | YES only | Embeddings | JDA response scale values |
| Internal construct | JDA | YES + NO | Embeddings | JDA response scale values |
| Internal construct | All | YES only | Embeddings | All response scale values |
| Internal construct | All | YES + NO | Embeddings | All response scale values |
| Codes only | IHRA | YES only | IHRA response scale values | Ordinal |
| Codes only | IHRA | YES + NO | IHRA response scale values | Ordinal |
| Codes only | Nexus | YES only | Nexus response scale values | Ordinal |
| Codes only | Nexus | YES + NO | Nexus response scale values | Ordinal |
| Codes only | JDA | YES only | JDA response scale values | Ordinal |
| Codes only | JDA | YES + NO | JDA response scale values | Ordinal |
| Codes only | All | YES only | All response scale values | Ordinal |
| Codes only | All | YES + NO | All response scale values | Ordinal |
| Codes + embeddings | IHRA | YES only | IHRA response scale values + embeddings | Ordinal |
| Codes + embeddings | IHRA | YES + NO | IHRA response scale values + embeddings | Ordinal |
| Codes + embeddings | Nexus | YES only | Nexus response scale values + embeddings | Ordinal |
| Codes + embeddings | Nexus | YES + NO | Nexus response scale values + embeddings | Ordinal |
| Codes + embeddings | JDA | YES only | JDA response scale values + embeddings | Ordinal |
| Codes + embeddings | JDA | YES + NO | JDA response scale values + embeddings | Ordinal |
| Codes + embeddings | All | YES only | All response scale values + embeddings | Ordinal |
| Codes + embeddings | All | YES + NO | All response scale values + embeddings | Ordinal |
| NLI convergent validity | IHRA | YES + NO | IHRA NLI entailment scores | Continuous |
| NLI convergent validity | Nexus | YES + NO | Nexus NLI entailment scores | Continuous |
| NLI convergent validity | JDA | YES + NO | JDA NLI entailment scores | Continuous |
| NLI convergent validity | All | YES + NO | All NLI entailment scores | Continuous |

## Results