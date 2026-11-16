import os
os.system("cls")

def calcular_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)

LISTA_NOTA = []

for i in range(3):
    nota = float(input('digite uma nota'))
    LISTA_NOTA.append(nota)

media = calcular_notas(LISTA_NOTA)

print(f'média: {media}')