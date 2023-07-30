```python
import pandas as pd
from research.teen_behavior_study import teen_behavior_data
from research.teen_workflow_analysis import teen_workflow_data
from research.teen_fun_flows import teen_fun_flow_data
from research.teen_sticky_features import teen_sticky_feature_data
from research.teen_annoyance_factors import teen_annoyance_data
from research.teen_interests import teen_interest_data
from research.teen_habits import teen_habit_data
from research.parent_expectations import parent_expectation_data
from research.impactful_features import impactful_feature_data

class UsageStatistics:
    def __init__(self):
        self.usage_data = pd.DataFrame()

    def getUsageData(self):
        self.usage_data['Teen Behavior'] = teen_behavior_data
        self.usage_data['Teen Workflow'] = teen_workflow_data
        self.usage_data['Teen Fun Flows'] = teen_fun_flow_data
        self.usage_data['Teen Sticky Features'] = teen_sticky_feature_data
        self.usage_data['Teen Annoyance Factors'] = teen_annoyance_data
        self.usage_data['Teen Interests'] = teen_interest_data
        self.usage_data['Teen Habits'] = teen_habit_data
        self.usage_data['Parent Expectations'] = parent_expectation_data
        self.usage_data['Impactful Features'] = impactful_feature_data

        return self.usage_data

    def displayUsageStatistics(self):
        print(self.usage_data.describe())

usage_statistic_data = UsageStatistics().getUsageData()
```