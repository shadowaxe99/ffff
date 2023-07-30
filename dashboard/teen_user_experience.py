import json
import datetime

from research.teen_interests import teen_interest_data
from research.teen_annoyance_factors import teen_annoyance_data
from research.teen_sticky_features import teen_sticky_feature_data

class UserExperienceSchema:
    def __init__(self, interest_data, annoyance_data, sticky_feature_data):
        self.interest_data = interest_data
        self.annoyance_data = annoyance_data
        self.sticky_feature_data = sticky_feature_data


def getUserExperienceData():
    user_experience_data = UserExperienceSchema(teen_interest_data, teen_annoyance_data, teen_sticky_feature_data)
    return user_experience_data


def update_user_experience_container(user_experience_data):
    user_experience_container = document.getElementById('userExperienceContainer')
    user_experience_container.innerHTML = json.dumps(user_experience_data.__dict__)


def update_user_experience_message():
    user_experience_data = getUserExperienceData()
    update_user_experience_container(user_experience_data)
    print('User experience updated at:', datetime.datetime.now())


update_user_experience_message()
