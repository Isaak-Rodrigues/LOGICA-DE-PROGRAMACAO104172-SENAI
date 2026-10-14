import os

os.system('cls')

print('= INSERINDO NOTAS NO VETOR =')
vetor_notas = []
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'digite a {i+1}ª nota: '))
    vetor_notas.append(nota)

media = sum(vetor_notas) / QUANTIDADE_NOTAS

print('= EXIBINDO AS NOTAS DO VETOR =')
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f'{posicao}ª nota: {nota}')


print(f'média: {media}')