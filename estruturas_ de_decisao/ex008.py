# 8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

precos = {}
for item in range(1,4):
    preco = float(input(f'Digite o valor do {item}° produto '))
    precos[item] = preco

id_mais_barato = min(precos, key=precos.get)
mais_barato = precos[id_mais_barato]

print(f'O produto mais barato é o número {id_mais_barato} com o preço de R${mais_barato:.2f}')
