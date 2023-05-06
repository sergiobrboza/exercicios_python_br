# 15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario = float(input('Quanto você recebe por hora trabalhada? R$'))
horas = int(input('Quantas horas você trabalha por mês? '))

salario_bruto = salario * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print('a. O salario bruto: R${}'.format(salario_bruto))
print('b. total pago ao IR: R${}'.format(ir))
print('c. O total pago ao INSS: R${}'.format(inss))
print('d. O total pago ao Sindicato: R${}'.format(sindicato))
print('e. O salario liquido: R${}'.format(salario_liquido))
