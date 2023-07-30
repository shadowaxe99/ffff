```python
import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2

class ImpactfulFeatureSchema:
    def __init__(self, feature_name, feature_importance):
        self.feature_name = feature_name
        self.feature_importance = feature_importance

def getImpactfulFeatureData():
    # Load the dataset
    data = pd.read_csv('teen_behavior_data.csv')

    # Define the target variable and the features
    y = data['target']
    X = data.drop('target', axis=1)

    # Use SelectKBest to get the top features
    selector = SelectKBest(chi2, k=10)
    selector.fit(X, y)

    # Get the feature names
    cols = selector.get_support(indices=True)
    features = X.iloc[:,cols]

    # Create a list of ImpactfulFeatureSchema
    impactful_feature_data = []
    for feature in features.columns:
        impactful_feature_data.append(ImpactfulFeatureSchema(feature, selector.scores_[cols].tolist()))

    return impactful_feature_data
```