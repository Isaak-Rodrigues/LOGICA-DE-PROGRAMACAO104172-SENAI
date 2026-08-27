import os

# LIMPA O TERMINAL
os.system('cls')

# ENTRADA
print ('= SOCICITANDO DADOS =')
primeiro_numero = float(input('Digite o seu primeiro número: '))
segundo_numero =float(input('Digite o seu segundo número'))

#PROCESSAMENTO
soma = primeiro_numero + segundo_numero
subtracao =  primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

# SAÍDA
print('\n= EXIBINDO DADOS =')
print('soma: ', soma)
print('subtração', subtracao)
print('multiplicação', multiplicacao)
print('divisão', divisao)