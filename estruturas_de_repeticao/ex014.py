# 14.Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
pares = impares = 0
for i in range (10):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print('O total de número pares que apareceram foi de:', pares)
print('E o total de números impares que apareceram foi de:', impares)