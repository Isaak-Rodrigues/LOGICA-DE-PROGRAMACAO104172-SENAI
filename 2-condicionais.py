import os

os.system('cls')

primeiro_numero = float(input('digite a primeira número '))
segundo_numero = float(input('digite a segunda número'))


soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero
maior = max (primeiro_numero, segundo_numero)
menor = min (primeiro_numero, segundo_numero)


print(f'\n Média {media} ')
print(f' Soma  {soma} ')
print(f' Produto {produto} ')
print(f' Maior número {maior} ')
print(f' Menor número {menor} ')


if primeiro_numero == segundo_numero:
    print(f'Os números são iguais')
else:
    print(f'Os números são diferentes')



