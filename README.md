# Startup Survival Rate Predictor 
## The Erdos Institute Data Science Boot Camp (Spring 2025)
### Authors
  - Sucharita Giri   
  - Amina Kurbidaeva

## Table of Contents
- [Introduction](#introduction)
- [Data](#data)
- [Modeling](#modeling)
- [Conclusions](#conclusions)
 
In this project, we use machine learning to predict the success rate of startups based on historical data. We identify key business features and build a predictive model to help stakeholders make informed, strategic decisions.
### Introduction

While startups drive innovation and economic growth, they also face a high risk of failure, making early-stage evaluation both crucial and challenging. Predicting which startups are likely to succeed can provide immense value to entrepreneurs, investors, and policymakers alike. This project aims to develop a data-driven model that forecasts a startup’s probability of survival using key features such as funding rounds, total funding amount, milestones achieved, team relationships, and company age. Given the highly imbalanced nature of the dataset—where successful startups make up only a small fraction—special attention was paid to model evaluation using metrics like F1 score, recall, and precision. By identifying the most impactful predictors of startup success, this project hopes to provide actionable insights and decision support for the startup ecosystem.

### Data

The dataset used for this project was sourced from open dataset on [Kaggle](https://www.kaggle.com/datasets/amirataha/startups/data) (original from Crunchbase). It includes key attributes related to startup performance, including funding rounds, total funding received in USD, number of milestones, team relationships, and company age. 

**Cleaning:**

We started off with a dataset that had quite a few missing values. Instead of trying to patch up everything, we decided to drop the columns that were mostly empty.

For the columns we did keep, we handled missing values in a reasonable and practical way. Depending on the type of data, we either filled in values with the mean, median, or a default fallback, so the model wouldn’t get confused with NaNs everywhere. Basically, we cleaned things up without overcomplicating it.

**Imbalance:**

Since the original data was highly imbalanced with only a small percentage of successful startups, care was taken to ensure the sample was representative enough to build a meaningful predictive model. Additional preprocessing was performed to clean missing values and prepare the data for analysis.

### Modeling

This document summarizes the performance evaluation of various machine learning models for predicting startup success. Multiple classification algorithms were assessed using 5-fold cross-validation to identify the most effective approach.


**Data Analysis:** 

Performed correlation analysis to identify predictive features across different datasets and implemented 5-fold stratified cross-validation with standardized features.

**Model Development:** 

Trained multiple algorithms (Logistic Regression, Random Forest, Gradient Boosting, SVM, KNN, Decision Tree, Naive Bayes, XGBoost), evaluating each with comprehensive metrics (accuracy, precision, recall, F1, AUC). For Logistic Regression, we tried to use status based and composite (status and age) based success definition, also USA and all countries approach.

**Model Optimization:** 

Conducted hyperparameter tuning via grid search on the best performing model, optimizing for F1 score to balance precision and recall.

**Interpretability:** 

Analyzed feature importance through coefficients or feature importance scores, visualizing key predictors across models.

**Performance Evaluation:** 

Generated confusion matrices, ROC curves, and precision-recall curves to thoroughly assess model discrimination ability and error patterns.

**Binary Classification Performance**

| Model                | Accuracy | Precision | Recall  | F1 Score | ROC AUC |
|----------------------|----------|-----------|---------|----------|---------|
| Gradient Boosting    | 70.9%    | 67.3%     | 20.0%   | 30.8%    | 66.4%   |
| XGBoost              | 70.6%    | 65.0%     | 20.2%   | 30.8%    | 65.4%   |
| SVM                  | 69.6%    | 65.9%     | 12.8%   | 21.4%    | 64.4%   |
| Naive Bayes          | 69.0%    | 59.8%     | 13.8%   | 22.5%    | 59.5%   |
| Logistic Regression  | 69.3%    | 69.8%     | 9.3%    | 16.4%    | 61.8%   |
| Random Forest        | 68.3%    | 53.0%     | 20.7%   | 29.8%    | 62.0%   |
| Decision Tree        | 68.2%    | 52.3%     | 20.3%   | 29.2%    | 58.5%   |
| KNN                  | 66.2%    | 46.4%     | 26.4%   | 33.7%    | 59.7%   |

**Logistic Regression Performance Across Folds**

| Fold    | Accuracy | Precision | Recall | F1 Score | AUC     |
|---------|----------|-----------|--------|----------|---------|
| 1       | 69.11%   | 65.91%    | 8.77%  | 15.48%   | 59.90%  |
| 2       | 69.09%   | 66.13%    | 8.56%  | 15.16%   | 59.66%  |
| 3       | 69.24%   | 68.32%    | 8.68%  | 15.40%   | 60.56%  |
| 4       | 69.42%   | 69.61%    | 9.22%  | 16.29%   | 60.23%  |
| 5       | 69.24%   | 66.96%    | 9.19%  | 16.16%   | 60.67%  |
| Average | 69.22%   | 67.39%    | 8.88%  | 15.70%   | 60.20%  |
| Std Dev | 0.12%    | 1.40%     | 0.27%  | 0.45%    | 0.38%   |

**Key Findings:**

1. **Composite Success Metric vs. Status-Based Definition**
The composite success metric outperformed the status-based definition likely because:

Richer Information Content: The composite metric incorporated both operational status AND company age/maturity, providing a more comprehensive view of success than status alone.

Reduced Noise: Status-only definitions can be misleading - some "active" companies may be struggling while technically operational, whereas the composite metric better distinguishes truly successful ventures.

Better Handling of Edge Cases: Companies in transitional states are more accurately classified with composite metrics that consider multiple dimensions of success.

Time Component: By including company age, the composite metric accounts for survival duration, a critical aspect of startup success often missing from binary status indicators.

2. **USA Companies vs. All Countries**
Focusing on USA companies yielded better results because:

Market Homogeneity: USA startups operate under a more consistent regulatory, economic, and business environment compared to a global dataset with diverse market conditions.

Data Quality: USA startup data tends to be more comprehensive and standardized, with fewer reporting gaps or inconsistencies.

Ecosystem Factors: Success factors may vary significantly across different startup ecosystems worldwide; limiting to one ecosystem creates a more consistent pattern for models to learn.

Reduced Confounding Variables: International differences in accounting practices, funding environments, and exit opportunities introduce confounding variables that models struggle to account for.

This suggests that regional context matters significantly in startup success prediction, and that multi-dimensional success definitions capture the complex nature of startup outcomes better than simplified status indicators.

3. **Model Comparison**:
   - Gradient Boosting and XGBoost achieved the best overall performance
   - KNN had the highest F1 score (33.7%), showing better balance between precision and recall
   - Logistic Regression had the highest precision but lowest recall
   - Composite success metric vs status based success definition showed better results

4. **Classification Challenges**:
   - All models struggled with the precision-recall tradeoff
   - Low recall values across models indicate difficulty in identifying successful startups
   - Models demonstrate modest discrimination ability (AUC between 58-66%)

5. **Model Stability**:
   - Cross-validation results show consistent performance across folds
   - Logistic regression exhibited very stable accuracy (std dev 0.12%)

6. **Best Model Selection**:
   - For balanced precision-recall: KNN
   - For best discrimination ability: Gradient Boosting
   - For highest precision: Logistic Regression
   - For overall performance: Gradient Boosting or XGBoost

### Conclusions

The results indicate that predicting startup success is challenging even with sophisticated machine learning approaches. While models can achieve reasonable accuracy (~70%), they struggle with identifying successful startups (low recall) without generating many false positives (maintaining precision).

Depending on the specific business requirements and the relative importance of precision vs. recall, different models might be preferred. For applications where missing successful startups is costly, KNN might be more appropriate despite its lower accuracy. For applications where false positives are more problematic, Gradient Boosting or Logistic Regression would be better choices.
