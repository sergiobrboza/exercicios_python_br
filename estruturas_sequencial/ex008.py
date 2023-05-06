# 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario = float(input('Quanto você recebe por hora trabalhada? R$'))
horas = int(input('Quantas horas você trabalha por mês? '))

print('Você recebe R${} por mês'.format(salario * horas))