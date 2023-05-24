# 10.Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
num1 += 1
for num in range(num1, num2):
    print(num, end=' ')