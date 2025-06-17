import re
import hashlib
import secrets
import logging

logging.basicConfig(filename='access.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def sanitize_input(input_str):

    if not re.match(r'^[a-zA-Z0-9_.-]{3,20}$', input_str):
        raise ValueError("Entrada inválida. Use apenas letras, números e os caracteres: _ . -")
    return input_str

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, stored_hash):
    return hashlib.sha256(password.encode()).hexdigest() == stored_hash

def log_event(event):
    logging.info(event)

def generate_session_token():
    return secrets.token_hex(32)