import os

# LIMPA O TERMINAL
os.system('cls')

# ENTRADA
primeira_nota = float(input('digite a primeira nota '))
segunda_nota = float(input('digite a  segunda nota'))
terceira_nota = float(input('digite a terceira nota'))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

#PROCESSAMENTO
if media >= 7:

    print('aprovado. ')
else:
    print('reprovado.')

# SAÍDA
print('media' , media)
