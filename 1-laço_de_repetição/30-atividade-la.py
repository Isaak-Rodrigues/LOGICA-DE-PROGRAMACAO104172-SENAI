import os
# import time ou usa o time.sleep

os.system('cls')
login_salvo = 'alex'
senha_salva = '332'

while True:
    login = (input('digite seu login'))
    senha = (input('digite sua senha'))
    
    if login == login_salvo and senha == senha_salva:
        print('bem vindo')
        break
    else:
        print('\nlogin ou senha inválido. ')
        print('tente novamente! \n')
        input('digite uma tecla para continuar')
        os.system('cls')



