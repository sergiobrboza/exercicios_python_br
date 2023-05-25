# 17.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
from math import factorial

while True:
    num = int(input('Digite um numero: '))
    f = factorial(num)
    print('O fatorial de {} é {}.'.format(num, f))