
# Feature Selection Report

## Summary
- Total features in original dataset: 86
- Numerical features analyzed: 47
- Categorical features included: 20
- Features removed due to multicollinearity: 9
- Final features selected: 48

## Top Features by Method

### Top 10 by Correlation with success_binary
funding_total_usd, funding_age_ratio, funding_efficiency, funding_rounds, days_to_first_funding, has_received_funding, is_us_based, has_strong_network, is_in_tech_state, relationship_density

### Top 10 by Random Forest Importance
overview_length, funding_total_usd, funding_efficiency, age_years, lng, funding_age_ratio, lat, relationships, description_length, tag_count

### Top 10 by ANOVA F-value
funding_total_usd, funding_age_ratio, funding_efficiency, funding_rounds, days_to_first_funding, has_received_funding, is_us_based, has_strong_network, days_from_creation_to_funding, is_in_tech_state

### Top 10 by Mutual Information
funding_total_usd, funding_efficiency, age_years, funding_age_ratio, lng, lat, has_website, relationships_per_million, relationship_density, category_diversity

## Highly Correlated Feature Pairs Removed
The following feature pairs had correlation coefficients above 0.8:
- funding_duration_days and funding_rounds: 0.810
- age_at_first_funding_years and days_to_first_funding: 0.823
- lifespan_days and age_years: 1.000
- funding_per_year and funding_total_usd: 0.877
- avg_funding_per_round and funding_total_usd: 0.919
- funding_rounds_per_year and funding_rounds: 0.898
- milestone_to_age_ratio and milestone_frequency: 1.000
- online_presence_score and has_twitter: 0.900
- online_presence_score and has_website: 0.894
