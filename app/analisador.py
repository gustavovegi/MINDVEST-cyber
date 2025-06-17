import os

def analisar_codigo(file_path):
    vulnerabilidades = {
        "eval(": "Uso de eval",
        "exec(": "Uso de exec",
        "pickle.load": "Uso de pickle.load",
        "input(": "Uso de input direto sem validação",
        "subprocess.Popen": "Uso de subprocess.Popen sem cuidado pode gerar execução de comandos externos"
    }

    achados = []

    with open(file_path, "r", encoding="utf-8") as f:
        linhas = f.readlines()
        for numero, linha in enumerate(linhas, start=1):
            for key, alerta in vulnerabilidades.items():
                if key in linha:
                    achados.append(f"[Linha {numero}] Possível vulnerabilidade: {alerta}")

    if achados:
        print(f"--- Vulnerabilidades encontradas no arquivo {file_path}: ---")
        for item in achados:
            print(item)
    else:
        print(f"Nenhuma vulnerabilidade crítica encontrada no arquivo {file_path}.")

arquivos = ["main.py", "utils.py"]

for arquivo in arquivos:
    if os.path.exists(arquivo):
        analisar_codigo(arquivo)
    else:
        print(f"Arquivo {arquivo} não encontrado.")