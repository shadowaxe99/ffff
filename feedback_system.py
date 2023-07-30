```python
import json
from flask import Flask, request
from schemas import FeedbackSchema

app = Flask(__name__)

feedback_data = []

@app.route('/feedback', methods=['POST'])
def getFeedbackData():
    feedback = request.get_json()
    errors = FeedbackSchema().validate(feedback)
    if errors:
        return {'error': errors}, 422
    feedback_data.append(feedback)
    return {'message': 'Feedback received', 'data': feedback}, 200

@app.route('/feedback', methods=['GET'])
def showFeedbackData():
    return json.dumps(feedback_data)

if __name__ == '__main__':
    app.run(debug=True)
```