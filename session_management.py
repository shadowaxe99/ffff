from flask import Flask, session, redirect, url_for, escape, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Set the secret key, which is needed for session to work
app.config['SECRET_KEY'] = 'super secret key'

# Set the encryption key
key = b'your-encryption-key'

@app.route('/')
def index():
    if 'username' in session:
        username = decrypt_data(session['username'], key)
        return 'Logged in as %s' % escape(username)
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = encrypt_data(request.form['username'], key)
        return redirect(url_for('index'))
    return '''<form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>'''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()


if __name__ == '__main__':
    app.run(debug=True)