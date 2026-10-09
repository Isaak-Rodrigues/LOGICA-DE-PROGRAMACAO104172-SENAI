import os

soma = 0
QUANTIDADE_NOTAS = 0
os.system('cls')

while True:
    print('''
=== MENU ===
S - inserir uma nota
n - calcular média aritmética
''')

    resposta = input('deseja inserir uma nota ?').lower()

    match resposta:
        case's':
            nota = float(input('digite uma nota'))
            soma += nota
            QUANTIDADE_NOTAS += 1
        case 'n':
            break
        case _:
            print('opção inválida!\n')
            input('pressione uma tecla para continuar ...')

if QUANTIDADE_NOTAS == 0:
    print('nao foram inseridas notas. \n')
else:
    media = soma / QUANTIDADE_NOTAS
    print(f'Média: {media}')



