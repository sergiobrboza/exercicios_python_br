# 24.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#  a.par ou ímpar;
#  b.positivo ou negativo;
#  c.inteiro ou decimal.

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))
opcao = input("Qual operação deseja realizar (+, -, *, /): ")



if opcao == '+':
    resultado = numero1 + numero2
elif opcao == '-':
    resultado = numero1 - numero2
elif opcao == '*':
    resultado = numero1 * numero2
elif opcao == '/':
    resultado = numero1 / numero2

if resultado < 0:
    print('O numero {} é negativo'.format(resultado))
else:
    print('O numero {} é positivo'.format(resultado))

par = resultado % 2

if par == 0:
    print('Esse numero é par')
else:
    print('Esse numero é impar')

if resultado == round(resultado):
    print('Esse numero é inteiro')
else:
    print('Esse numero é decimal')

