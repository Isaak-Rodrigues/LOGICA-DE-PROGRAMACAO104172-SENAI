import os

os.system('cls')




primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número'))
terceiro_numero = float(input('Digite o terceiro número'))

maior = max (primeiro_numero, segundo_numero, terceiro_numero)
menor = min (primeiro_numero, segundo_numero, terceiro_numero)

print(f'\n primeiro número: {primeiro_numero}')
print(f'segundo número: {segundo_numero}')
print(f'terceiro número: {terceiro_numero}')
print(f'Maior número {maior}')
print(f'Menor número {menor}')
