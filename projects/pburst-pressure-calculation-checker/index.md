---
layout: single
title: Pburst Pressure Calculation Checker
author_profile: true
---

## About This Project
This project is still under construction. Any ILI data analyst or pipeline integrity engineer can run this application to check ILI vendor provided pressure calculations. The application reads in an Excel file, predicts column mapping and allows the user to confirm or override mapping, and then calculates the selected Burst Pressure methods. The calculated Pburst values are compared to the Pbust values reported in the Excel sheet, with statistics such and min, mean, and max delta provided.

Metric and Imperial units are supported. 

Users can currently download the zipped application and run it locally on your desktop. Application is still in testing phase and has not been officially released. 

## Repository
Repository link: [Pburst Pressure Checker Repository](https://github.com/sgillihan/Pipeline_Pfail_Pressure_Checker.git)

## Technologies Used
The application is structured as a local client–server pair: a Python/FastAPI backend serving both the REST API and the compiled React frontend as static files, launched in a native desktop window via pywebview. When packaged with PyInstaller, the entire application ships as a single folder with no external runtime dependencies.

