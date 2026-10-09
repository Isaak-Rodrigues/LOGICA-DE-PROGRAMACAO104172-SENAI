import os
import time

os.system('cls')

soma = 0
QUANTIDADE_NUMEROS = 0

while True:
    os.system('cls')
    numero = int(input('digite um numero'))
    if numero >= 0:
        soma += numero
        QUANTIDADE_NUMEROS += 1
        time.sleep(2)
    else:
        break

if QUANTIDADE_NUMEROS == 0:
    print('nao foram inseridas notas. \n')
else:
    media = soma / QUANTIDADE_NUMEROS
    print(f'Média: {media}')

errado
