# Startup Survival Rate Predictor 
## The Erdos Institute Data Science Boot Camp (Spring 2025)
### Authors
  - Sucharita Giri   
  - Amina Kurbidaeva

## Table of Contents
- [Introduction](#introduction)
- [Data](#data)
- [Modeling](#modeling)
- [Usage](#usage)
- [Data Description](#data-description)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

**Project Overview:**  

### Introduction

While startups drive innovation and economic growth, they also face a high risk of failure, making early-stage evaluation both crucial and challenging. Predicting which startups are likely to succeed can provide immense value to entrepreneurs, investors, and policymakers alike. This project aims to develop a data-driven model that forecasts a startup’s probability of survival using key features such as funding rounds, total funding amount, milestones achieved, team relationships, and company age. Given the highly imbalanced nature of the dataset—where successful startups make up only a small fraction—special attention was paid to model evaluation using metrics like F1 score, recall, and precision. By identifying the most impactful predictors of startup success, this project hopes to provide actionable insights and decision support for the startup ecosystem.

### Data

The dataset used for this project was sourced from open dataset on [Kaggle](https://www.kaggle.com/datasets/amirataha/startups/data) (original from Crunchbase). It includes key attributes related to startup performance, including funding rounds, total funding received in USD, number of milestones, team relationships, and company age. 

**Cleaning**
We started off with a dataset that had quite a few missing values. Instead of trying to patch up everything, we decided to drop the columns that were mostly empty.

For the columns we did keep, we handled missing values in a reasonable and practical way. Depending on the type of data, we either filled in values with the mean, median, or a default fallback, so the model wouldn’t get confused with NaNs everywhere. Basically, we cleaned things up without overcomplicating it.

**Imbalance**
Since the original data was highly imbalanced with only a small percentage of successful startups, care was taken to ensure the sample was representative enough to build a meaningful predictive model. Additional preprocessing was performed to clean missing values and prepare the data for analysis.

**Stakeholders**  

**KPI** 

**Modeling**  

**Results and Outcomes**  

**Future Directions**  
