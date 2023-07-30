```python
import json
from flask import Flask, request, jsonify
from schemas import FeatureUpdateSchema

app = Flask(__name__)

feature_update_data = []

@app.route('/feature_updates', methods=['POST'])
def update_feature():
    data = request.get_json()
    errors = FeatureUpdateSchema().validate(data)
    if errors:
        return jsonify(errors), 400
    feature_update_data.append(data)
    return jsonify({"message": "Feature update data added", "data": data}), 201

@app.route('/feature_updates', methods=['GET'])
def get_feature_updates():
    return jsonify(feature_update_data)

if __name__ == '__main__':
    app.run(debug=True)
```