import os

os.system('cls')

login_correto = 'alex'
senha_correta = '3223'

print(' = TELA DE CADASTROS = ')
login_cadastrado = input ('digite seu login')
senha_cadastrada = input ('digite sua senha')

while True:
    os.system('cls')
    print(' = TELA PARA LOGIN = ')
    login_informado = input('digite seu login')
    senha_informada = input('digite seu senha')

    login_correto == login_informado == login_cadastrado
    senha_correta == senha_informada == senha_cadastrada

    if login_correto and senha_correta:
        print('bem vindo')
        break
    else:
        print('login ou senha incorretas. \ntente novamente! \n')
        input('presione uma tecla pra continuar...')