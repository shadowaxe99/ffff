```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class TeenHabitSchema:
    def __init__(self, habit_name, frequency, duration, impact_level):
        self.habit_name = habit_name
        self.frequency = frequency
        self.duration = duration
        self.impact_level = impact_level

def getTeenHabitData():
    # Load the data
    data = pd.read_csv('teen_habit_data.csv')

    # Create a LabelEncoder object
    le = LabelEncoder()

    # Convert the categorical columns into numeric
    data['habit_name'] = le.fit_transform(data['habit_name'])
    data['frequency'] = le.fit_transform(data['frequency'])
    data['duration'] = le.fit_transform(data['duration'])
    data['impact_level'] = le.fit_transform(data['impact_level'])

    # Split the data into training and testing sets
    X = data.drop('impact_level', axis=1)
    y = data['impact_level']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a RandomForestClassifier object
    clf = RandomForestClassifier(n_estimators=100)

    # Train the model
    clf.fit(X_train, y_train)

    # Predict the impact level of the habits
    y_pred = clf.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)

    # Export the data
    teen_habit_data = []
    for index, row in data.iterrows():
        teen_habit_data.append(TeenHabitSchema(row['habit_name'], row['frequency'], row['duration'], row['impact_level']))

    return teen_habit_data, accuracy
```