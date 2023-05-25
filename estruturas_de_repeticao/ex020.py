# 20.Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
from math import factorial

while True:
    num = int(input('Digite um numero: '))
    if num > 16:
        print('O numero informado é maior que 16, tente novamente.')
    else:
        f = factorial(num)
        print('O fatorial de {} é {}.'.format(num, f))
    acao = input('Deseja fazer novamente S/N: ').upper()

    if acao == 'N':
        print('Fim')
        break