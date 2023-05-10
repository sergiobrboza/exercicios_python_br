# 16.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#  a.Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#  b.Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#  c.Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#  d.Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

a = float(input('Digite um valor para a : '))

if a == 0:
    print('Essa equação não é de segundo grau.')
else:
    b = float(input('Digite um valor para b : '))
    c = float(input('Digite um valor para c : '))
    delta = (b)**2 - 4*(a)*(c)

if delta < 0:
    print('Essa equação naõ possui raizes reais')
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação possui apenas uma raiz real: x = {x:.2f}")
else:
    x1 = ( -b + math.sqrt(delta)) / (2 * a)
    x2 = ( -b - math.sqrt(delta)) / (2 * a)
    print('As duas raizes são: {}, {}'.format(x1, x2))
