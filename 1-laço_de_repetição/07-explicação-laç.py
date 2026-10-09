import os
import time

os.system('cls')

so = 0
soma_geral = 0
quantidade_geral = 0
quantidade_pares = 0
quantidade_impares = 0


while True:
    os.system('cls')
    numero = int(input('digite um numero'))

    if numero >= 0:
        quantidade_geral += 1
        soma_geral += numero

        if numero % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero
        else:
            quantidade_impares += 1
        time.sleep(2)
    else:
        break

if quantidade_geral == 0:
    print('não foram inseridos numeros. \n')
else:
    media_geral = soma_geral / quantidade_geral
    media_geral = soma_geral / quantidade_geral
    print (f'media geral: {media_geral:}')
    print (f'media pares: {media_pares:}')
    print (f'quantidade de pares: {quantidade_pares}')
    print (f'quantidade de impares: {quantidade_impares:}')


errado