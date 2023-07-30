```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class TeenBehaviorStudy:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None
        self.model = RandomForestClassifier()

    def load_data(self):
        self.data = pd.read_csv(self.data_path)
        return self.data

    def preprocess_data(self):
        label_encoder = LabelEncoder()
        for column in self.data.columns:
            if self.data[column].dtype == 'object':
                self.data[column] = label_encoder.fit_transform(self.data[column])
        return self.data

    def split_data(self):
        X = self.data.drop('behavior', axis=1)
        y = self.data['behavior']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def evaluate_model(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

    def get_teen_behavior_data(self):
        return self.data

if __name__ == "__main__":
    teen_behavior_study = TeenBehaviorStudy('teen_behavior_data.csv')
    teen_behavior_data = teen_behavior_study.load_data()
    teen_behavior_data = teen_behavior_study.preprocess_data()
    X_train, X_test, y_train, y_test = teen_behavior_study.split_data()
    teen_behavior_study.train_model(X_train, y_train)
    accuracy = teen_behavior_study.evaluate_model(X_test, y_test)
    print(f'Model Accuracy: {accuracy}')
```
