# 23.Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input('Digite qualquer numero: '))

if numero == round(numero):
    print('Esse numero é inteiro')
else:
    print('Esse numero é decimal')