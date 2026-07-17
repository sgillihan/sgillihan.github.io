---
layout: single
title: "Chess Insights: Result Predictors and Play Sequences by Player Ranking"
author_profile: true
---

## About This Project
This project analyzes more than 84 million standard-rated chess games from the February 2026 Lichess database to investigate which game characteristics are associated with wins, losses, and draws. The original dataset contained approximately 184 GB of decompressed PGN data, requiring an efficient workflow for parsing, cleaning, transforming, and storing large-scale data.

Using Python, I converted the raw PGN records into structured Parquet datasets and engineered features such as player rating difference, rating group, game length, time-control category, opening moves, and early move sequences. I then used descriptive statistics and grouped comparisons to examine how outcomes varied across player skill levels and game conditions.

The project also explores predictive models, including logistic regression, decision trees, and random forests, using accuracy, precision, recall, F1 score, and confusion matrices for evaluation. In addition to prediction, the analysis emphasizes interpretability by identifying common openings and move sequences associated with different outcomes and determining whether those patterns change across rating groups.

## Project Documentation
- [Project Proposal](/projects/data_mining-chess/Part2ProjectProposal_SGillihan.pdf)
- [Project Progress Update](/projects/data_mining-chess/Part_3_Progress_Update_SGillihan.pdf)
- [Chess Insights Pipeline Notebook](/projects/data_mining-chess/chess_mining_pipeline.html)

## Technologies Used
- Python
- pandas
- NumPy
- python-chess
- scikit-learn
- Matplotlib
- Seaborn
- Zstandard
- Parquet

## Repository
Repository link: [Chess Insights](https://github.com/sgillihan/CSPB4502_DataMiningProject)

