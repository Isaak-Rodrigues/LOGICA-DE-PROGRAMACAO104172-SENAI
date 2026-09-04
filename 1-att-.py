import os

# LIMPA O TERMINAL
os.system('cls')

login = (input('digite o seu login: '))
senha = (input('digite sua senha: '))

login_salvo = 'isaak'
senha_salva = '2332'

login_esta_correto = login == login_salvo
senha_esta_correta = senha == senha_salva

if login_esta_correto and senha_esta_correta:
    print('bem vindo')
else:
    print('login ou senha invalido')
