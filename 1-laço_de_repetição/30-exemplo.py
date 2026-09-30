import os

os.system('cls')

while True:
    numero = int (input('digite um número entre 1 e 10'))
    if numero < 1 or numero > 10:
        print('\nnúmero invalido,tente novamente. ')
    else:
        print('o número está entre 1 e 10. ')
        break # serve pra parar o laço de repetição

print('= FIM =')