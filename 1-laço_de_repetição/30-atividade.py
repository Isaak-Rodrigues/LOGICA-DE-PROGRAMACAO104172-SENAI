import os
import time
os.system('cls')


while True:
    nota = int (input('digite um número entre 0 e 10. '))
    if nota < 0  or nota > 10:
        print('\ntente novamente')
        
    else:
        print('o número esta entre 0 e 10')
        print(f'nota: {nota}')
        break