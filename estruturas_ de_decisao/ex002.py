# 2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Digite um numero positivo ou negativo: '))

if valor < 0:
    print('O numero {} é negativo'.format(valor))
elif valor == 0:
    print('Esse numero é neutro')
else:
    print('O numero {} é positivo'.format(valor))