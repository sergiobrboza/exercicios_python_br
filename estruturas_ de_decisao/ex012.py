# 12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#  Desconto do IR:
#  Salário Bruto até 900 (inclusive) - isento
#  Salário Bruto até 1500 (inclusive) - desconto de 5%
#  Salário Bruto até 2500 (inclusive) - desconto de 10%
#  Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        #  Salário Bruto: (5 * 220)        : R$ 1100,00
        #  (-) IR (5%)                     : R$   55,00  
        #  (-) INSS ( 10%)                 : R$  110,00
        #  FGTS (11%)                      : R$  121,00
        #  Total de descontos              : R$  165,00
        #  Salário Liquido                 : R$  935,00

valor_horas = float(input('Valor por hora trabalhada: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))

salario_bruto = valor_horas * horas_trabalhadas

inss_porcentagem = '10%'
fgts_porcentagem = '11%'

inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    ir_porcentagem = 'Isento'
    ir = 0
    salario_liguido = salario_bruto - inss
    desconto = ir + inss

if salario_bruto > 900 and salario_bruto <= 1500:
    ir_porcentagem = '5%'
    ir = salario_bruto * 0.05
    salario_liguido = salario_bruto - ir - inss
    desconto = ir + inss

if salario_bruto > 1500 and salario_bruto <= 2500:
    ir_porcentagem = '10%'
    ir = salario_bruto * 0.1
    salario_liguido = salario_bruto - ir - inss
    desconto = ir + inss

else:
    ir_porcentagem = '20%'
    ir = salario_bruto * 0.2
    salario_liguido = salario_bruto - ir - inss
    desconto = ir + inss

print('Salario Bruto: ({:.2f} * {})         : R${}'.format(valor_horas, horas_trabalhadas, salario_bruto))
print('(-) IR ({})                          : R${}'.format(ir_porcentagem, ir))
print('(-) INSS ({})                        : R${}'.format(inss_porcentagem, inss))
print('FGTS ({})                            : R${}'.format(fgts_porcentagem, fgts))
print('Total de desconto                    : R${}'.format(desconto))
print('Salario Liguido                      : R${}'.format(salario_liguido))