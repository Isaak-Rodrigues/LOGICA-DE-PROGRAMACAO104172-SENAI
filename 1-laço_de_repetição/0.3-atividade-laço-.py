import os

os.system('cls')

QUANTIDADE_DE_NOTAS = 3
soma= 0

for i in range (QUANTIDADE_DE_NOTAS):
    soma += float(input('escreva suas notas. '))

media = soma / QUANTIDADE_DE_NOTAS

if media >= 7.0:
    print('aprovado')
elif media <= 4.0:
    print('reprovado')
elif media <= 6.0:
    print('recuperação')

print(f'\nSUAS MEDIAS')
print(f'soma : {soma}')
print(f'media : {media}')
