import os
os.system("cls")

def verificacao(numero):
    if numero < 0:
        resultado = 'negativo'
    elif numero == 0:
        resultado = 'neutro'
    else:
        resultado = 'positivo'
    return resultado

print('= SOLICITANDO DADOS =')
numero = int(input('digite um número: '))
resultado = verificacao(numero)

print('\n = EXIBINDO DADOS =')
print(f"o número{numero} é {resultado}")