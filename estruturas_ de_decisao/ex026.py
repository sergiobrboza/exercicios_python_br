# 26.Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#  a.Álcool:
#  b.até 20 litros, desconto de 3% por litro
#  c.acima de 20 litros, desconto de 5% por litro
#  d.Gasolina:
#  e.até 20 litros, desconto de 4% por litro
#  f.acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input('Escolha o combustivel:\n [ G ] Gasolina\n [ A ] Alcool\n ').upper()
litros = float(input('Litros vendidos: '))

if combustivel == 'G':

    porcentagem1 = 2.5 - (2.5 * 0.04)
    porcentagem2 = 2.5 - (2.5 * 0.06)

    if litros <= 20:
        desconto = litros * porcentagem1
    else:
        desconto = litros * porcentagem2

    print('Você colocou {} litros de gasolina e a gasolina saiu custando R${:.2f}'.format(litros, desconto))

elif combustivel == 'A':

    porcentagem1 = 2.5 - (2.5 * 0.03)
    porcentagem2 = 2.5 - (2.5 * 0.05)

    if litros <= 20:
        desconto = litros * porcentagem1
    else:
        desconto = litros * porcentagem2

    print('Você colocou {} litros de alcool e o alcool saiu custando R${:.2f}'.format(litros, desconto))
else:
    print('Erro, tente novamente!!!')