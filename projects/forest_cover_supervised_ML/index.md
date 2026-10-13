---
layout: single
title: "Forest Cover Predictions Using Decision Tree, Random Forest, and SVM Models"
description: "Comparing Decision Tree, Random Forest, and SVM models in scikit-learn to predict forest cover type from the UCI Covertype dataset, reaching 96.7% accuracy."
author_profile: true
---

## About This Project
This project uses the UCI Forest Covertype dataset to compare Decision Tree, Random Forest, and Support Vector Machine models for predicting forest cover type from environmental and geographic features. The dataset contains more than 581,000 observations and 54 predictors, including elevation, slope, hydrology distances, wilderness areas, and soil types.

The analysis includes exploratory data analysis, class-imbalance evaluation, feature scaling, hyperparameter tuning with cross-validation, repeated stratified sampling, and scalability testing. Model performance was evaluated using accuracy, macro precision, recall, F1 score, training time, and per-class results.

Random Forest produced the strongest overall performance, reaching approximately 96.7% test accuracy and a 0.943 macro F1 score on the final test set. Feature-importance analysis using impurity importance, permutation importance, and mutual information consistently identified elevation as the most influential predictor.

## Project Documentation
- [Forest Cover Prediction Notebook](/projects/forest_cover_supervised_ML/Forest_Cover_Prediction_SGillihan_final.html)

## Technologies Used
- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn

## ML Models Used
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

## Repository
Repository link: [Forest Cover Prediction](https://github.com/sgillihan/CSPB4622_Project1_Forest_Cover.git)

