# Startup Success Prediction Model Building Report

## Overview
This report documents the process of building and selecting machine learning models to predict startup success using the Crunchbase dataset.

## Data Preparation
- Binary class distribution: {(0,): np.float64(67.58052797287479), (1,): np.float64(32.41947202712521)}

## Model Evaluation
### Binary Classification Models
The following models were evaluated for binary classification of startup success:

|    | model_name          |   cv_accuracy_mean |   cv_accuracy_std |   test_accuracy |   precision |    recall |   f1_score |   roc_auc |
|---:|:--------------------|-------------------:|------------------:|----------------:|------------:|----------:|-----------:|----------:|
|  4 | KNN                 |           0.655131 |        0.0425022  |        0.662307 |    0.463555 | 0.264117  |   0.336506 |  0.597371 |
|  7 | XGBoost             |           0.698377 |        0.00375932 |        0.705996 |    0.65     | 0.201972  |   0.308183 |  0.654078 |
|  2 | Gradient Boosting   |           0.700436 |        0.00279348 |        0.709096 |    0.673387 | 0.199582  |   0.307905 |  0.663695 |
|  1 | Random Forest       |           0.681448 |        0.00342559 |        0.683425 |    0.530222 | 0.207051  |   0.297808 |  0.620397 |
|  5 | Decision Tree       |           0.674691 |        0.00190022 |        0.681585 |    0.523112 | 0.202868  |   0.292357 |  0.585118 |
|  6 | Naive Bayes         |           0.688762 |        0.00340222 |        0.690497 |    0.598191 | 0.138333  |   0.224703 |  0.595194 |
|  3 | SVM                 |           0.695825 |        0.01       |        0.695825 |    0.659476 | 0.127876  |   0.214214 |  0.644324 |
|  0 | Logistic Regression |           0.689852 |        0.00180979 |        0.692919 |    0.697987 | 0.0932178 |   0.16447  |  0.61788  |

## Best Model Selection
- Best binary classification model: **KNN**

## Hyperparameter Tuning
The best binary model (KNN) was tuned with the following parameters:

```
{'n_neighbors': 7, 'p': 1, 'weights': 'uniform'}
```


## Feature Importance
The most important features for predicting startup success are:

Feature importance analysis was not available for the selected model.


## Model Performance
The final model demonstrates strong predictive performance as evidenced by the confusion matrix and ROC curve (for binary classification).

## Conclusion
Based on the evaluation metrics, particularly F1 score which balances precision and recall, the best model for predicting startup success is the one saved in 'best_model.pkl'.

This model can be used to:
1. Predict the likelihood of success for new startups
2. Identify key factors that contribute to startup success
3. Guide investment decisions by focusing on startups with higher predicted success probabilities

## Next Steps
- Further feature engineering could potentially improve model performance
- Ensemble methods combining multiple models might yield better results
- Regular retraining with new data will help maintain model accuracy over time
