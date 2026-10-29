import os
os.system('cls')

lista_produtos = []

while True:
    input ('pressione uma tecla para continuar ...')
    os.system('cls')

    print('''
=== MERCADINHO DENDEZEIROS ===
1 - Cadrastar produtos
2 - listar produtos
0 - Sair
''')

    opcao = int(input('escolha uma opção'))

    match opcao:
        case 1:
            print('\n== CADASTRAR UM PRODUTO ==')
            # strip()retira os espaços vazios no final
            # upper todas as letras maiusculas
            nome = input('nome do produto: ').strip().upper()
            #.append(nome)adiciona o nome do produto na lista
            lista_produtos.append(nome)
            print('produto cadastrado com sucesso')
        case 2:
            print('\n== LISTA DE PRODUTOS ==')
            for produto in lista_produtos:
                print(f'nome: {produto['nome']}, Preço {produto['preço']}')
                input('precione ENTER para continuar ...')
        case 0:
            print('saindo de programa')
            break