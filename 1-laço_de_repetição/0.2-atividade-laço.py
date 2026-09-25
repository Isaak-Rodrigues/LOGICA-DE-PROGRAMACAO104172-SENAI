import os

os.system('cls')

print(f'\nsocilicitando notas')

QUANTIDADE_DE_NOTAS = 4
soma = 0.0

for i in range (QUANTIDADE_DE_NOTAS):
    soma += float(input('escreva suas notas. '))

media = soma / QUANTIDADE_DE_NOTAS

print(f'\nSUAS MEDIAS')
print(f'soma : {soma}')
print(f'media : {media}')
