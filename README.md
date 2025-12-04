# Attacker Behavioral Profiling in SSH Honeypots

## Overview
This repository contains the notebook explore.ipynb, which performs exploratory analysis, feature engineering, dimensionality reduction, and clustering on SSH honeypot attack sessions.
The goal is to extract meaningful behavioral patterns and automatically identify attacker types such as bots, script kiddies, and skilled human operators.

What the Notebook Does

1. Data Preparation

- Loading raw SSH honeypot logs

- Cleaning and normalizing command data

- Handling missing values and irrelevant fields

2. Feature Engineering

- Extraction of behaviorally relevant indicators, including:

- Reconnaissance features (scanning, enumeration commands)

- Exploitation features (wget, curl, tftp, busybox, payload execution)

- Error patterns (failed commands, permission errors)

- Correction patterns (typos, backspaces, repeated edits)

- Session-level metrics (duration, command diversity, recon/exploit ratio)

3. Dimensionality Reduction

- Applying PCA to inspect variance structure

- Visualizing feature separability

4. Unsupervised Behavioral Clustering

- Clustering attacker sessions using HDBSCAN

- Identifying groups that correspond to attacker profiles

- Manual interpretation of clusters 


## Purpose

This is a project in the course Cybersecurity at the University of Bologna (UNIBO) with the research question: 
1. Can clustering methods effectively group SSH honeypot attackers into meaningful behavioral profiles such as bots, script kiddies, and skilled human operators based on their command sequences, interaction patterns, and session-level behavioral features?


## Dataset 

The project uses the Cyberlab Honeypot Dataset, which contains real SSH attack logs collected from a honeypot environment and it's public dataset. 
Link: https://zenodo.org/records/3687527 

Description: Large-scale dataset (9 months, 50 nodes) showcasing diverse attacker behaviors

Format: JSON logs with timestamps, commands, and session metadata

- The specific file used in this project is: cyberlab_2020-02-29.json

File location: 

- Inside the project structure, the dataset is stored in: ../dataset/cyberlab_2020-02-29.json

Load the data: 
```bash
with open("../dataset/cyberlab_2020-02-29.json") as f:
    data = json.load(f)
``` 


## How to Run
Install dependencies:

```bash
pip install -r requirements.txt

```

## Collaborators
- .... länka till er



