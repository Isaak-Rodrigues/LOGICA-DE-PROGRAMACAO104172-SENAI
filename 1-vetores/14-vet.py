import os

os.system('cls')

print('= INSERIDO NÚMEROS NO VETOR =')
vetor_notas = []

for i in range(3):
    nota = float(input('Digite uma nota: '))
    vetor_notas.append(nota)

media = sum(vetor_notas) / 3

for i in range(3):
    print(f'nota: {vetor_notas[i]}')

print(f'média: {media}')