# contested-antisemitism
Detecting Antisemitism: Multi-Aspect Operationalization of a Contested Concept via Natural Language Inference

| Section | Subsections |
|---|---|
| [Proposal Draft](https://www.overleaf.com/read/hyxgchsjpvwz#91c7ce) | |
| [Abstract](#abstract) |
| [Methodology](#methodology) | [Pilot](#pilot) · [Pilot Codebook](#pilot-codebook) · [Data Collection](#data-collection) |
| [Repository Structure](#repository-structure) |
| [Instructions](#instructions) | |
| [Results](#results) |
| [Discussion](#discussion) |
| [Job IDs](#job-ids) | |

## Abstract

## Methodology

### [Pilot Codebook](https://github.com/jwrampino/contested-antisemitism/blob/main/pilot/PILOT_CODEBOOK.md)

### [Pilot](https://github.com/jwrampino/contested-antisemitism/blob/main/pilot/PILOT_MODELS.md)

### [Data Collection](https://github.com/jwrampino/contested-antisemitism/blob/main/collection/)

## Repository Structure

```
contested-antisemitism/
├── collection/                                 # Data collection pipeline
│   ├── data/
│   │   ├── 4chan/
│   │   ├── 8kun/
│   │   ├── bluesky/
│   │   ├── truthsocial/
│   │   ├── corpus_raw.parquet                      # Open Measures full corpus
│   │   ├── corpus_deduped.parquet                  # Deduped Open Measures corpus
│   │   └── cursor_index.json                       # Checkpoint
│   ├── openmeasures.ipynb                        # Open Measures collection script 
│   ├── query.py                                  # Open Measures query config
│   └── reddit.ipynb                              # Reddit collection script (WiP)
├── pilot/                                      # Pilot scripts
│   ├── batches/                                  # LLM batch label results
│   │   ├── results/                                # Labels by batch
│   │   └── batch_index.json                        # API query index
│   ├── data/
│   │   └── ucberkeley-dlab_target_jewish.csv       # Pilot dataset
│   ├── features/                                 # Features for all pilot models
│   │   ├── pca/                                   
│   │   ├── raw_scaled/  
│   │   ├── embeddings.csv                          
│   │   ├── code_features.csv                      # LLM labels OHE
│   │   ├── nli_zeroshot_scores.csv                # NLI v1 model scores
│   │   ├── nli_zeroshot_scores_v2.csv             # NLI v2 model scores
│   │   ├── nli_zeroshot_scores_v1_prefix.csv      # v1 using corrected hypotheses
│   │   ├── nli_zeroshot_scores_v2_prefix.csv      # v2 using corrected hypotheses
│   │   ├── reranker_scores_bge.csv
│   │   ├── reranker_scores_qwen.csv
│   │   └── targets_and_folds.csv
│   ├── test/                                     # Intra and inter-LLM agreement
│   ├── viz/
│   ├── config.py                                 # Batch instructions for LLMs
│   ├── label.ipynb                               # LLM batch labeling
│   ├── nli_config.py                             # Hypotheses for NLI (_prefix)
│   ├── nli.ipynb                                 # NLI scoring colab
│   ├── reranker.ipynb                            # Reranker test colab
│   ├── models.ipynb                              # Pilot analysis and ablation study
│   ├── PILOT_CODEBOOK.md                         # Initial codebook for pilot configs
│   └── PILOT_MODELS.md                           # Outlines contents of models.ipynb
├── .gitignore
├── README.md
└── environment.yml
```

## Instructions

```
conda env create -f environment.yml
conda activate anti
```

## Results

## Discussion

## Job IDs