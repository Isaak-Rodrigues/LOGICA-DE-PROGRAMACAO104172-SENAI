import os

# LIMPA O TERMINAL
os.system('cls')

media = float(input('digite sua media: '))
falta = int(input('digite suas faltas '))

limite_de_faltas = 40
media_de_aprovacao = 7.0

if media >= media_de_aprovacao and falta <= limite_de_faltas:
    resultado = 'aprovado'
else:
    resultado = 'reprovado'

print(f'\nresultado: {resultado}')