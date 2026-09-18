import os

os.system('cls')

print ('= TABUADA = ')
numero = int(input('digite um numero. '))

print(f'\nsoma')

for i in range (1, 11):
    print(f'{numero} + {i} = {numero + i}')
print(f'\nsubtração')
for i in range (1, 11):
    print(f'{numero} - {i} = {numero - i}')
print(f'\nmultiplicação')
for i in range (1, 11):
    print(f'{numero} * {i} = {numero * i}')
print(f'\ndivisão')
for i in range (1, 11):
    print(f'{numero} / {i} = {numero / i}')
