# antisemitism_classifier
A Multi-Definitional Framework for Antisemitism and Comparative Platform Enforcement

| Section | Subsections |
|---|---|
| [Proposal Draft](https://www.overleaf.com/read/hyxgchsjpvwz#91c7ce) | |
| [Abstract](#abstract) |
| [Literature Review](#literature-review) | |
| [Methodology](#methodology) | [Pilot](#pilot) · [Codebook](#codebook) |
| [Repository Structure](#repository-structure) |
| [Instructions](#instructions) | |
| [Results](#results) |
| [Discussion](#discussion) |
| Job IDs | |

## Abstract

## Literature Review
  
Anti-semitism  
Chandra et al (2021)      https://doi.org/10.1145/3447535.3462502  
Salhi and Goldhorn (2025) https://doi.org/10.11647/obp.0447.06  
Kennedy et al. (2020)     https://hatespeech.berkeley.edu/  
Liu et al. 2024           https://arxiv.org/pdf/2405.03794  
Reiger et al              https://doi.org/10.1177/20563051211052906  
Culbert                   https://arxiv.org/abs/2307.03556  
jikeli                    https://doi.org/10.36190/2021.14  
becker                    https://doi.org/10.3389/fcomm.2025.1729279 | https://doi.org/10.26613/jca/5.1.105  
Zannettou                 https://arxiv.org/abs/1809.01644  
  
multimodal  
Chandra et al (2021)      https://doi.org/10.1145/3447535.3462502  
Salhi and Goldhorn (2025) https://doi.org/10.11647/obp.0447.06  
  
social media (far-right attitudes)
colley and moore          https://doi.org/10.1177/1461444820948803
reiger et al              https://doi.org/10.1177/20563051211052906


llm labeling

  
## Methodology

### [Pilot](https://github.com/jwrampino/antisemitism_classifier/blob/main/pilot/PILOT.md)

### [Codebook](https://github.com/jwrampino/antisemitism_classifier/blob/main/CODEBOOK.md)

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
│   │   └── ucberkeley-dlab_target_jewish.csv       # Pilot dataset
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
│   ├── nli.ipynb                                 # Pilot NLI models
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