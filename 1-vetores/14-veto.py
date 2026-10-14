import os

os.system('cls')

print('= INSERIDO NÚMEROS NO VETOR =')
vetor_livros = []

for i in range(5):
    livro = input(f'digite o nome do {i+1}ºlivro')
    vetor_livros.append(livro)

print('= INSERINDO NÚMEROS NO VETOR =')
for indice, livro in enumerate (vetor_livros, start=1):
    print(f'valor: {valor}')