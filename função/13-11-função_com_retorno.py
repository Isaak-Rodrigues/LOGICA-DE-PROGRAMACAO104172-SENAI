import os
os.system('cls')

# função com parametro e com retorno
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

print('= SOLICITANDO DADOS =')
nota1 = float(input('digite a primeira nota'))
nota2 = float(input('digite a segunda nota'))

# usando a função com parametro e
# inserindo o retorno na variável soma
soma = calcular_notas('nota1, nota2')

print('= EXEIBINDO DADOS =')
print(f'soma: {soma}')