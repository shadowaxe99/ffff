import json
from flask import Flask, render_template, request
from research import teen_behavior_study, teen_workflow_analysis, teen_fun_flows, teen_sticky_features, teen_annoyance_factors, teen_interests, teen_habits, parent_expectations, impactful_features

import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    teen_behavior_data = teen_behavior_study.getTeenBehaviorData()
    teen_workflow_data = teen_workflow_analysis.getTeenWorkflowData()
    teen_fun_flow_data = teen_fun_flows.getTeenFunFlowData()
    teen_sticky_feature_data = teen_sticky_features.getTeenStickyFeatureData()
    teen_annoyance_data = teen_annoyance_factors.getTeenAnnoyanceData()
    teen_interest_data = teen_interests.getTeenInterestData()
    teen_habit_data = teen_habits.getTeenHabitData()
    parent_expectation_data = parent_expectations.getParentExpectationData()
    impactful_feature_data = impactful_features.getImpactfulFeatureData()

    dashboard_data = {
        'teen_behavior': teen_behavior_data,
        'teen_workflow': teen_workflow_data,
        'teen_fun_flow': teen_fun_flow_data,
        'teen_sticky_feature': teen_sticky_feature_data,
        'teen_annoyance': teen_annoyance_data,
        'teen_interest': teen_interest_data,
        'teen_habit': teen_habit_data,
        'parent_expectation': parent_expectation_data,
        'impactful_feature': impactful_feature_data
    }

    return render_template('dashboard.html', data=dashboard_data)

if __name__ == '__main__':
    print('Server started at:', datetime.datetime.now())
    app.run(debug=True)
