import os

os.system('cls')

while True:
    print('''
        | = MENU =
Opção      |produtos   |preços
1          |macarrão   |R$ 3,80
2          |arroz      |R$ 5,30
3          |uvas       |R$ 2,50
4          |abacaxi    |R$ 4,95
5          |banana     |R$ 3,75
''')
    opcao = input('digite a opção desejada:')

    match opcao:
        case '1':
            print('produto: macarrão \npreço:R$ 3,80')
            break
        case '2':
            print('produto: arroz    \npreço:R$  5,30')
            break
        case '3':
            print('produto: uvas     \npreço:R$ 2,50 ')
            break
        case '4':
            print('produto: abacaxi  \npreço:R$  4,95 ')
            break
        case '5':
            print('produto: banana   \npreço:R$ 3,75 ')
            break
        case _:
            print('opção invalida ')