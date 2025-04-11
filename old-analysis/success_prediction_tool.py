
# Startup Success Prediction Tool
# Generated on 2025-04-08

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.preprocessing import StandardScaler

def predict_startup_success(startup_data):
    '''
    Predict the success probability of a startup based on its characteristics.

    Parameters:
    -----------
    startup_data : dict
        Dictionary containing startup features. Required keys are:
        - funding_total_usd: Total funding received in USD
        - age_years: Age of the startup in years
        - funding_rounds: Number of funding rounds
        - has_received_funding: Whether the startup has received any funding (0/1)
        - is_us_based: Whether the startup is based in the US (0/1)
        - is_in_tech_state: Whether the startup is in a tech-focused state (0/1)
        - relationships: Number of relationships in the dataset
        - has_website: Whether the startup has a website (0/1)
        - has_strong_network: Whether the startup has a strong network (0/1)
        - overview_length: Length of the company overview text
        - text_quality_score: Quality score of the text (1-5)

    Returns:
    --------
    dict: Dictionary containing:
        - success_probability: Probability of success (0-1)
        - success_class: Predicted success class (high_success, moderate_success, unsuccessful)
        - top_factors: List of top factors contributing to the prediction
    '''
    # Load the model and preprocessing pipeline
    try:
        model = pickle.load(open('best_model.pkl', 'rb'))
        pipeline = pickle.load(open('preprocessing_pipeline.pkl', 'rb'))
    except FileNotFoundError:
        return {
            "error": "Model files not found. Please ensure best_model.pkl and preprocessing_pipeline.pkl are in the current directory."
        }

    # Define required features
    required_features = [
        'funding_total_usd', 'age_years', 'funding_rounds', 'has_received_funding',
        'is_us_based', 'is_in_tech_state', 'relationships', 'has_website',
        'has_strong_network', 'overview_length', 'text_quality_score'
    ]

    # Check if all required features are provided
    missing_features = [f for f in required_features if f not in startup_data]
    if missing_features:
        return {
            "error": f"Missing required features: {', '.join(missing_features)}"
        }

    # Create a DataFrame with the startup data
    df = pd.DataFrame([startup_data])

    # Calculate derived features
    if df['funding_total_usd'].values[0] > 0 and df['age_years'].values[0] > 0:
        df['funding_efficiency'] = df['funding_total_usd'] / df['age_years']
        df['funding_age_ratio'] = df['funding_total_usd'] / (df['age_years'] ** 2)
    else:
        df['funding_efficiency'] = 0
        df['funding_age_ratio'] = 0

    if df['relationships'].values[0] > 0:
        df['relationship_density'] = df['relationships'] / (df['age_years'] + 1)
        df['relationships_per_million'] = df['relationships'] / (df['funding_total_usd'] / 1000000 + 0.1)
    else:
        df['relationship_density'] = 0
        df['relationships_per_million'] = 0

    # Apply preprocessing
    try:
        X_processed = pipeline.transform(df)
    except Exception as e:
        return {
            "error": f"Error in preprocessing: {str(e)}"
        }

    # Make prediction
    try:
        success_prob = model.predict_proba(X_processed)[0, 1]
        success_class = 'high_success' if success_prob > 0.75 else ('moderate_success' if success_prob > 0.5 else 'unsuccessful')

        # Determine top contributing factors
        feature_importance = [
            ('funding_total_usd', 0.439),
            ('funding_efficiency', 0.226),
            ('funding_age_ratio', 0.209),
            ('age_years', 0.179),
            ('funding_rounds', 0.137),
            ('relationships', 0.122),
            ('is_us_based', 0.100),
            ('has_received_funding', 0.097),
            ('has_website', 0.086),
            ('has_strong_network', 0.079)
        ]

        # Filter to features that are positive for this startup
        top_factors = []
        for feature, importance in feature_importance:
            if feature in startup_data:
                if isinstance(startup_data[feature], (int, float)):
                    if startup_data[feature] > 0:
                        top_factors.append((feature, importance))
                elif startup_data[feature]:  # For boolean features
                    top_factors.append((feature, importance))

        # Sort by importance and take top 5
        top_factors = sorted(top_factors, key=lambda x: x[1], reverse=True)[:5]

        return {
            "success_probability": float(success_prob),
            "success_class": success_class,
            "top_factors": [f[0] for f in top_factors]
        }
    except Exception as e:
        return {
            "error": f"Error in prediction: {str(e)}"
        }

# Example usage
if __name__ == "__main__":
    # Example startup data
    example_startup = {
        'funding_total_usd': 5000000,
        'age_years': 3,
        'funding_rounds': 2,
        'has_received_funding': 1,
        'is_us_based': 1,
        'is_in_tech_state': 1,
        'relationships': 10,
        'has_website': 1,
        'has_strong_network': 1,
        'overview_length': 500,
        'text_quality_score': 4
    }

    result = predict_startup_success(example_startup)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Success Probability: {result['success_probability']:.2%}")
        print(f"Success Class: {result['success_class']}")
        print(f"Top Contributing Factors:")
        for factor in result['top_factors']:
            print(f"- {factor}")
