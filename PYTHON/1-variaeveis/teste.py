import os
os.system("cls")

#SOLICITANDO DADOS
nome,sobrenome = input("digite seu nome e sobrenome: ").split()
#sobre_nome = input("digite seu sobrenome: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

#MOSTRANDO DADOS

print("nome e sobrenome: ", nome, sobrenome)
#print("sobrenome: ", sobre_nome)
print("idade:", idade)
print("peso", peso)
print("altura", altura)