import os

# LIMPA O TERMINAL
os.system('cls')

# ENTRADA
primeiro_numero = float(input('digite a primeira número '))
segundo_numero = float(input('digite a segunda número'))


#PROCESSAMENTO

soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
    
else:
    maior = segundo_numero
    menor =primeiro_numero


# SAÍDA
print(f'\n Média {media} ')
print(f'\n Soma  {soma} ')
print(f'\n Produto {produto} ')
print(f'\n Maior número {maior} ')
print(f'\n Menor número {menor} ')



