# 18.Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
numeros = []
num = int(input('Digite a quantidade de números no conjunto: '))

for i in range(num):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)
print('O maior valor é', maior)
print('O menor valor é', menor)
print('O resultado da soma dos valores é', soma)