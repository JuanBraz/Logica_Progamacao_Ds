import random
import os


# Recebe um numero aleatório entre 0 e 100
numero_premiado = random.randint(0,100)
num_tentados = []
tentativas = 5
tempo = 30



os.system('cls')
while True: 
    ent_usuario = int(input('Digite um número: '))
    print()
    if ent_usuario == numero_premiado:
        print('Você ganhou!')
        break
    elif tentativas == 0:
        print(f'Você perdeu, o numero premiado era {numero_premiado}')
        break
    else:
        print('Você não acertou o número!')
        # adiociona o numero tentado na lista
        num_tentados.append(ent_usuario)
        tentativas -=1
        
        # verifica se o numero digitado é maior ou menor
        if ent_usuario > numero_premiado:
            print('Digite um número menor! ')
        else:
            print('Digite um número maior!')
            
print ('Fim de jogo')
print(f'Voce tentou os numeros: {num_tentados}')
print(f'Voce precisou de: {len(num_tentados)} tentativas')