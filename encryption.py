from cryptography.fernet import Fernet

# Function to generate and return a Fernet encryption key
def generate_encryption_key():
    return Fernet.generate_key()

# Function to encrypt user data
def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Function to decrypt user data
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data