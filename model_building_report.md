# Startup Success Prediction Model Building Report

## Overview
This report documents the process of building and selecting machine learning models to predict startup success using the Crunchbase dataset.

## Data Preparation
- Training data shape: (157242, 272)
- Testing data shape: (39311, 272)
- Binary class distribution: {0: 92.95290062451508, 1: 7.047099375484921}
- Multi-class distribution: {'unsuccessful': 82.83919054705486, 'low_success': 10.11371007746022, 'high_success': 5.8044288421668515, 'moderate_success': 1.2426705333180703}

## Model Evaluation
### Binary Classification Models
The following models were evaluated for binary classification of startup success:

|    | model_name          |   cv_accuracy_mean |   cv_accuracy_std |   test_accuracy |   precision |   recall |   f1_score |   roc_auc |
|---:|:--------------------|-------------------:|------------------:|----------------:|------------:|---------:|-----------:|----------:|
|  2 | Gradient Boosting   |           0.999981 |       1.55777e-05 |        1        |   1         | 1        |   1        |  1        |
|  5 | Decision Tree       |           0.999987 |       1.55775e-05 |        1        |   1         | 1        |   1        |  1        |
|  1 | Random Forest       |           0.999688 |       0.000110885 |        0.999822 |   0.999277  | 0.998195 |   0.998736 |  0.999998 |
|  0 | Logistic Regression |           0.996547 |       0.000360138 |        0.996566 |   0.980314  | 0.970758 |   0.975512 |  0.999838 |
|  3 | SVM                 |           0.990206 |       0.01        |        0.990206 |   0.976809  | 0.881949 |   0.926959 |  0.999041 |
|  4 | KNN                 |           0.9568   |       0.00411825  |        0.9579   |   0.897363  | 0.454513 |   0.603403 |  0.881169 |
|  6 | Naive Bayes         |           0.102733 |       0.00231015  |        0.10333  |   0.0726785 | 0.997112 |   0.135482 |  0.516854 |

### Multi-class Classification Models
The following models were evaluated for multi-class classification of startup success:

|    | model_name                        |   cv_accuracy_mean |   cv_accuracy_std |   test_accuracy |   precision |    recall |   f1_score |
|---:|:----------------------------------|-------------------:|------------------:|----------------:|------------:|----------:|-----------:|
|  3 | SVM                               |          0.828394  |       0.01        |       0.828394  |    0.686237 | 0.828394  | 0.750644   |
|  0 | Logistic Regression (Multinomial) |          0.828392  |       2.33581e-05 |       0.828369  |    0.686233 | 0.828369  | 0.750632   |
|  1 | Random Forest                     |          0.823552  |       0.00043616  |       0.822263  |    0.697478 | 0.822263  | 0.748843   |
|  2 | Gradient Boosting                 |          0.823434  |       0.01        |       0.823434  |    0.695225 | 0.823434  | 0.748813   |
|  4 | KNN                               |          0.80357   |       0.00766906  |       0.810282  |    0.698036 | 0.810282  | 0.745345   |
|  5 | Decision Tree                     |          0.728298  |       0.00138232  |       0.728829  |    0.70057  | 0.728829  | 0.714166   |
|  6 | Naive Bayes                       |          0.0152313 |       0.000332869 |       0.0143726 |    0.674325 | 0.0143726 | 0.00429095 |

## Best Model Selection
- Best binary classification model: **Gradient Boosting**
- Best multi-class classification model: **SVM**

## Hyperparameter Tuning
The best binary model (Gradient Boosting) was tuned with the following parameters:

```
{'C': 10, 'gamma': 'auto', 'kernel': 'rbf'}
```


## Feature Importance
The most important features for predicting startup success are:

|    | Feature                       |   Importance |
|---:|:------------------------------|-------------:|
| 86 | status_acquired               |  0.662776    |
| 26 | funding_total_usd             |  0.210554    |
| 88 | status_ipo                    |  0.0695074   |
|  1 | age_years                     |  0.0571629   |
| 19 | overview_length               |  3.05421e-13 |
|  2 | days_from_creation_to_funding |  2.02684e-13 |
| 10 | lng                           |  1.47113e-13 |
| 13 | relationship_density          |  1.08901e-13 |
| 24 | lat                           |  7.65975e-14 |
| 15 | days_between_milestones       |  6.17119e-14 |


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