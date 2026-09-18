import os

os.system("cls")

print('= solicitando dados = ')
valor = float(input('digite o valor: '))

# CALCULANDO
# desconto de 10%
desconto = valor * 0.10
valor_do_desconto = valor - desconto


print('\n= EXIBINDO DADOS = ')
print('valor com desconto de 10%: ', valor_do_desconto)