import os
os.system("cls")

# soma = 0

print('= ESCREVA OS NÚMEROS QUE DESEJA SOMAR')
primeiro_numero = float(input('digite o primeiro numero'))
segundo_numero = float(input('digite o segundo numero'))

soma = primeiro_numero + segundo_numero
subtrasao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

print('= MOSTRANDO RESULTADOS =')

print(f'soma  {soma}')
print(f'subtrasão {subtrasao}')
print(f'multiplicação {multiplicacao}')
print(f'divisão {divisao}')