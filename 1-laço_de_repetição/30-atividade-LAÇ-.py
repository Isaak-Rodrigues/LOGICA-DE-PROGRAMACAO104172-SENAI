import os

os.system('cls')

os.system('cls')
login_salvo = 'colle'
senha_salva = '233'
tentativas = 1

while True:
    if tentativas <= 3:
        print(f'tentativas: {tentativas}')
        login = (input('digite seu login'))
        senha = (input('digite sua senha'))
        tentativas +=1
        if login == login_salvo and senha == senha_salva:
            print('bem vindo')
            break
        else:
            print('\nlogin ou senha inválido. ')
            print('tente novamente! \n')
            input('digite uma tecla para continuar')
            os.system('cls')
    else:
        print('= FIM =')
        break