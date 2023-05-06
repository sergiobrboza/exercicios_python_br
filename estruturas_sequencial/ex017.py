# 17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil, floor

tamanho_m2 = int(input('Quantos metros quadrados tem a área? '))

litros = ceil(tamanho_m2 / 6)
latas = ceil(litros / 18)
preco1 = latas * 80


galoes = ceil(litros / 3.6)
preco2 = galoes * 25

litros_resto = floor(tamanho_m2 / 6)

print('Voce gastara {}L de tinta, tera que comprar {} latas e gastará R${:.2f} se comprar latas de 18 litros'.format(litros, latas, preco1))
print('Voce gastara {}L de tinta, tera que comprar {} galões e gastará R${:.2f} se comprar galões de 18 litros'.format(litros, galoes, preco2))
print('Voce utilizara {} galões e {} latas e gastará R${:.2f} com sobra de 10%'.format())