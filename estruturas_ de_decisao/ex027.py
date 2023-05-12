# 27.Uma frutaria está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#  Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#  Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#  Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

kg_morango = float(input('Quantos Kg de morango? '))
kg_maca = float(input('Quantos Kg de maçã? '))

kg_total = kg_morango + kg_maca

if kg_total < 8:

    if kg_morango <= 5:
        valor_morango = kg_morango * 2.5
    else:
        valor_morango = kg_morango * 2.2

    if kg_maca <= 5:
        valor_maca = kg_maca * 1.8
    else:
        valor_maca = kg_maca * 1.5

    valor_total = valor_maca + valor_morango

else: 
    if kg_morango <= 5:
        valor_morango = kg_morango * 2.25
    else:
        valor_morango = kg_morango * 1.98

    if kg_maca <= 5:
        valor_maca = kg_maca * 1.62
    else:
        valor_maca = kg_maca * 1.35

    valor_total = valor_maca + valor_morango

print('O cliente comprou {}Kg de maçâ e {}Kg de morango, ele pagará: R${}'.format(kg_maca, kg_morango, valor_total))    