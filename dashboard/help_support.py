```python
import json
from flask import Flask, request, jsonify
from schemas import HelpSupportSchema

app = Flask(__name__)

help_support_data = []

@app.route('/help_support', methods=['POST'])
def add_help_support():
    new_help_support = request.get_json()
    help_support_data.append(new_help_support)
    return jsonify(new_help_support), 201

@app.route('/help_support', methods=['GET'])
def get_help_support_data():
    return jsonify(help_support_data), 200

@app.route('/help_support/<int:help_support_id>', methods=['PUT'])
def update_help_support(help_support_id):
    updated_help_support = request.get_json()
    help_support_data[help_support_id] = updated_help_support
    return jsonify(updated_help_support), 200

@app.route('/help_support/<int:help_support_id>', methods=['DELETE'])
def delete_help_support(help_support_id):
    del help_support_data[help_support_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```