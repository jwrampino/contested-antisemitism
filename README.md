# contested-antisemitism
Detecting Antisemitism: Multi-Aspect Operationalization of a Contested Concept via Natural Language Inference

| Section | Subsections |
|---|---|
| [Proposal Draft](https://www.overleaf.com/read/hyxgchsjpvwz#91c7ce) | |
| [Abstract](#abstract) |
| [Methodology](#methodology) | [Pilot](#pilot) · [Codebook](#codebook) |
| [Repository Structure](#repository-structure) |
| [Instructions](#instructions) | |
| [Results](#results) |
| [Discussion](#discussion) |
| [Job IDs](#job-ids) | |

## Abstract

## Methodology

### [Codebook](https://github.com/jwrampino/contested-antisemitism/blob/main/CODEBOOK.md)

### [Pilot](https://github.com/jwrampino/contested-antisemitism/blob/main/pilot/PILOT.md)

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
│   │   ├── ucberkeley-dlab_target_jewish.csv       # Pilot dataset
│   │   ├── nli_zeroshot_scores.csv                 # Pilot NLI scores
│   │   ├── 
│   │   ├── 
│   ├── features/                                 # Features for all pilot models
│   │   ├── pca/
│   │   ├── raw_scaled/
│   │   ├── code_features.csv
│   │   ├── embeddings.csv
│   │   └── targets_and_folds.csv
│   ├── test/                                     # Intra and inter-LLM agreement
│   ├── viz/
│   ├── config.py                                 # Batch instructions for LLMs
│   ├── nli_config.py                             # Hypotheses for NLI (_prefix)
│   ├── label.ipynb                               # LLM batch labeling
│   ├── nli.ipynb                                 # NLI scoring colab
│   ├── reranker.ipynb                            # Reranker test colab
│   ├── models.ipynb                              # Pilot analysis and ablation study
│   ├── PILOT_CODEBOOK.md                         # Initial codebook for pilot configs
│   └── PILOT.md                                  # Outlines contents of models.ipynb
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