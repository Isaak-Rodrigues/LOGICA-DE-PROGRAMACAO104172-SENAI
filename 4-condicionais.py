import os

os.system('cls')

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número'))
maior = max (primeiro_numero, segundo_numero)
menor = min (primeiro_numero, segundo_numero)

print(f'\n Os numeros são {primeiro_numero} e {segundo_numero}')
print(f'Maior número {maior}')
print(f'Menor número {menor}')


