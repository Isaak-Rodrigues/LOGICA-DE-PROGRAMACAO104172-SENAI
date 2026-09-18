import os

os.system('cls')

idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Não podem votar')

elif idade < 18:
    print('Voto opicional')

elif idade <=65:
    print('Voto obrigatorio')

else:
    print('Não e obrigado a votar')


