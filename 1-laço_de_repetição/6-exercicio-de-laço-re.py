import os
import time

os.system('cls')

numero = int(input('digite um numero. '))
for i in range (numero,0,-1):
    print(f'o número é: {i}')

    time.sleep(1)

print('fim')

