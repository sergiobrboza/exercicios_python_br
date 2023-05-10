# 17.Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Descubra se o ano é BISSEXTO: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))