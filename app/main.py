import json
from utils import sanitize_input, hash_password, verify_password, log_event, generate_session_token

try:
    with open('users.json', 'r') as file:
        users = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    users = {}

def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)

def register():
    try:
        username = sanitize_input(input("Novo username: "))
        if username in users:
            print("Usuário já existe.")
            return
        password = sanitize_input(input("Senha: "))
        users[username] = hash_password(password)
        save_users()
        log_event(f"Novo usuário registrado: {username}")
        print("Usuário registrado com sucesso.")
    except ValueError as e:
        print(e)

def login():
    try:
        username = sanitize_input(input("Username: "))
        password = sanitize_input(input("Senha: "))

        if username not in users:
            print("Usuário não encontrado.")
            log_event(f"Tentativa de login falhou para usuário: {username}")
            return
        
        if verify_password(password, users[username]):
            token = generate_session_token()
            log_event(f"Login bem-sucedido: {username} - Token: {token}")
            print(f"Login OK! Token de Sessão: {token}")
        else:
            print("Senha incorreta.")
            log_event(f"Senha incorreta para usuário: {username}")
    except ValueError as e:
        print(e)

def main():
    while True:
        print("\n[1] Registrar\n[2] Login\n[3] Sair")
        choice = input("Escolha: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()