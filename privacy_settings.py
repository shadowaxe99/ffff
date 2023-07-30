```python
import json
from flask import Flask, request, jsonify
from schemas import PrivacySettingSchema

app = Flask(__name__)

privacy_setting_data = {}

@app.route('/privacy_settings', methods=['GET'])
def get_privacy_setting_data():
    return jsonify(privacy_setting_data)

@app.route('/privacy_settings', methods=['POST'])
def update_privacy_setting_data():
    global privacy_setting_data
    new_data = request.get_json()
    errors = PrivacySettingSchema().validate(new_data)
    if errors:
        return jsonify(errors), 400
    privacy_setting_data = new_data
    return jsonify(privacy_setting_data), 200

if __name__ == '__main__':
    app.run(debug=True)
```