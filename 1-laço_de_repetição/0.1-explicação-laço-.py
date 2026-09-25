import os

os.system('cls')

print ('ACUMULANDO VALORES EM UMA VARIÁVEL. ')
soma = 0
# print(f'VALOR INICIAL DA VARIÁVEL SOMA: {soma}')

for i in range (3):
    soma += int(input('\ndigite um  numero para somar: '))

# soma += numero
# print(f'VALOR TEMPORáRIO DA VARIÁVEL SOMA: {soma}')

print(f'\nvalor final da variavel soma: {soma}')

