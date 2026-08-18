# antisemitism_classifier
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

### [Codebook](https://github.com/jwrampino/antisemitism_classifier/blob/main/CODEBOOK.md)

### [Pilot](https://github.com/jwrampino/antisemitism_classifier/blob/main/pilot/PILOT.md)

### [Data Collection](https://github.com/jwrampino/antisemitism_classifier/blob/main/collection/)

## Repository Structure

```
antisemitism_classifier/
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
│   │   └── nli_zeroshot_scores.csv                 # Pilot NLI scores
│   ├── features/                                 # Features for all pilot models
│   │   ├── pca/
│   │   ├── raw_scaled/
│   │   ├── code_features.csv
│   │   ├── embeddings.csv
│   │   └── targets_and_folds.csv
│   ├── test/                                     # Intra and inter-LLM agreement
│   ├── viz/
│   ├── config.py                                 # Batch instructions
│   ├── label.ipynb                               # LLM labeling notebook
│   ├── models.ipynb                              # Pilot models
│   ├── nli.ipynb                                 # NLI scoring colab
│   ├── PILOT.md
│   └── viz.ipynb
├── .gitignore
├── CODEBOOK.md
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