# Success Metrics Definition Report

## Overview
This report documents how success metrics were defined for the startup analysis project using the Crunchbase dataset. Multiple success metrics were created to capture different aspects of startup success, and a composite metric was developed to provide a more comprehensive measure.

## Success Metrics Defined

## Composite Success Metric

A composite success score was created by combining multiple factors:

- **Status Component**: 3 points for acquired/IPO companies
- **Age Component**:
             - 2 points for top 10%
             - 1 point for top 25%

### Success Score Distribution
success_score
0    34964
1     6521
2     4236
3     3310
4     1326
5     1256

### Binary Success Classification
- **Definition**: Companies with a success score ≥ 1
- **Success Rate**: 32.26% of companies classified as successful

## Conclusion

The composite success metric provides a balanced approach to measuring startup success, accounting for multiple dimensions while handling the challenge of missing data. The binary and multi-class labels derived from this metric will serve as target variables for predictive modeling in subsequent analysis steps.
