import time

# Funcao para retornar o oposto da escolha
def inverter_escolha(escolha):
    if escolha == "par":
        return "impar"
    elif escolha == "impar":
        return "par"

# Boas Vindas

print("Bem vindo ao Cassino do Gordao")
time.sleep(2)
print("Hoje estamos com odds de 5 pra 1. Para jogar e muito simples")
time.sleep(2)

#Loop principal do GAME

while True:
    escolha_invertida = None

    #Loop Para garantir uma escolha valida

    while escolha_invertida is None:

    #perguntar pro apostador
        escolha_usuario = input("\n Voce escolhe 'par' ou 'impar'? ").strip().lower()
        escolha_invertida = inverter_escolha(escolha_usuario)

        if escolha_invertida is None:
            print("Vc eh burro? 'par' ou 'impar ")
    
    #mensagem do resultado

    print(f"Voce escolheu '{escolha_usuario}', mas o resultado foi '{escolha_invertida}', a casa ganha ")

    #Loop para garantir que o usuario jogue novamente ou saia
    while True:
        jogar_novamente = input("\nDeseja jogar de novo? (s/n): ").strip().lower()
        
        if jogar_novamente in ['s', 'n']:
            break
        else: print("Burro, 's' para sim ou 'n' para nao")

    if jogar_novamente == 'n':
        print("Obrigado, ate a proxima")
        break