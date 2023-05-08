# 8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o primeiro valor: R$"))
preco2 = float(input("Digite o segundo valor: R$"))
preco3 = float(input("Digite o terceiro valor: R$"))

if preco1 <= preco2 and preco1 <= preco3:
    print('O primeiro produto é mais barato')
elif preco2 <= preco1 and preco2 <= preco3:
    print('O segundo produto é mais barato')
else:
    print('O terceiro produto é mais barato')