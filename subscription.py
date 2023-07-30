from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscription.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subscription_level = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    name = data['name']
    email = data['email']
    subscription_level = data['subscription_level']
    expiration_date = data['expiration_date']

    user = User(name=name, email=email, subscription_level=subscription_level, expiration_date=expiration_date)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Subscription successful'})


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.get_json()
    email = data['email']

    user = User.query.filter_by(email=email).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Unsubscription successful'})
    else:
        return jsonify({'message': 'User not found'})


if __name__ == '__main__':
    app.run(debug=True)