# 1.Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

maior = num1

if num2 > num1:
    maior = num2
else:
    print('Os valores são iguais')
print('O maior numero é:',maior)