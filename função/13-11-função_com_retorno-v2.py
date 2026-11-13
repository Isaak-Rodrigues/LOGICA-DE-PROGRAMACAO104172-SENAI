import os
os.system("cls")
# função com parametro e com retorno
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) /2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = 'aprovado'
    else:
        resultado = 'reprovado'
    return resultado

print('= SOLICITANDO DADOS =')
nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

# usando a função com parametro e
# inserindo o retorno na variável soma
media = calcular_notas(nota1, nota2)
situacao = verificar_resultado(media)


print('= EXEIBINDO DADOS =')
print(f'media: {media}')
print(f'resultado: {situacao}')

# if media >= 7:
#     print('aprovado')
# else:
#     print('reprovado')