# 11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#   Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 280,00 (incluindo) : aumento de 20%
#   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

salario = float(input('Qual é o salario do colaborador? R$'))

aumento1 = salario * 0.2
aumento2 = salario * 0.15
aumento3 = salario * 0.1
aumento4 = salario * 0.05

if salario <= 280:
    porcentagem = '20%'
    valor_de_aumento = aumento1
    reajustado = salario + aumento1
    
if salario > 280 and salario <= 700:
    porcentagem = '15%'
    valor_de_aumento = aumento2
    reajustado = salario + aumento2
    
if salario > 700 and salario <= 1500:
    porcentagem = '10%'
    valor_de_aumento = aumento3
    reajustado = salario + aumento3
    
if salario > 1500:
    porcentagem = '5%'
    valor_de_aumento = aumento4
    reajustado = salario + aumento4

print('O antigo salario era de: R$',salario)
print('A porcentagem de aumento foi de:',porcentagem)

print('O valor de aumento foi de: R$',valor_de_aumento)
print('O salario final é de: R$',reajustado)