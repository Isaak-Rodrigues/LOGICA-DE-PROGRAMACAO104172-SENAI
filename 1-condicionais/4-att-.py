import os

# LIMPA O TERMINAL
os.system('cls')

nota = float(input('digite uma nota '))

if 0 <= nota <= 10:
    print("nota" , nota)

else:
    print('a nota deve ser entre 0 e 10 ')
