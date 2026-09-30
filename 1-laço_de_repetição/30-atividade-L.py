import os

os.system('cls')
# QUANTIDADE_NOTA = 2
# soma = 0
# for i in range (QUANTIDADE_NOTA):
#     while True:
#         nota = float(input(f'digite o {i+1}º número entre 0 e 10. '))
#         if nota >= 0  and  nota <= 10:
#             soma = soma + nota
#             break
#         else:
#             print('nota invalida, tente de novo')
# media = soma / QUANTIDADE_NOTA
# print(f'media {media}')



QUANTIDADE_NOTA = 2
soma = 0
for i in range (QUANTIDADE_NOTA):
    while True:
        nota = float(input(f'digite o {i+1}º número entre 0 e 10. '))
        if nota < 0  or  nota > 10:
            print('\nnota inválida, tente novamente')
        else:
            soma = soma + nota
            break
media = soma / QUANTIDADE_NOTA
print(f'media {media}')


