import re
import hashlib
import secrets
import logging

# Configuração de log
logging.basicConfig(filename='access.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def sanitize_input(input_str):
    # Apenas caracteres seguros
    if not re.match(r'^[a-zA-Z0-9_.-]{3,20}$', input_str):
        raise ValueError("Entrada inválida. Use apenas letras, números e os caracteres: _ . -")
    return input_str

def hash_password(password):
    salt = secrets.token_hex(16)
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return f"{salt}${hash_obj.hex()}"

def verify_password(password, stored_hash):
    salt, hash_value = stored_hash.split('$')
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return new_hash.hex() == hash_value

def log_event(event):
    logging.info(event)

def generate_session_token():
    return secrets.token_hex(32)