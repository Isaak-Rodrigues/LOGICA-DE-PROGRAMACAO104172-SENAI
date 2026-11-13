import os
os.system("cls")

def calcular_soma(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

def calcular_subtracao(nota1, nota2):
    resultado = nota1 - nota2
    return resultado

def calcular_multiplicacao(nota1, nota2):
    resultado = nota1 * nota2
    return resultado

def calcular_divisao(nota1, nota2):
    # if nota2 == 0:
    #     return 'atençao! divisão por zero'
    return  nota1 / nota2

print('= SOLICITANDO DADOS =')
nota1 = float(input('digite a primeira nota'))
nota2 = float(input('digite a segunda nota'))


soma = calcular_soma (nota1, nota2)
subtracao = calcular_subtracao (nota1, nota2)
multplicacao = calcular_multiplicacao (nota1, nota2)
divisao = calcular_divisao (nota1, nota2)

print('= EXEIBINDO DADOS =')
print(f'soma: {soma}')
print(f'subtração: {subtracao}')
print(f'multiplicação: {multplicacao}')
print(f'divisão: {divisao}')