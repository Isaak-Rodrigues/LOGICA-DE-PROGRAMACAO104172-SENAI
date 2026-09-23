import os

os.system('cls')

# verificando os numeros pares

print('MOSTRANDO OS NÚMEROS PARES ENTRE 1 E 10')
for i in range(1,11):
    if i % 2 == 0:
        print(f'{i} é par.')