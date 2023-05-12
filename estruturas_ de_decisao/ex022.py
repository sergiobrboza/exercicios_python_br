# 22.Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input('Digite um numero inteiro: '))

par = numero % 2

if par == 0:
    print('Esse numero é par')
else:
    print('Esse numero é impar')