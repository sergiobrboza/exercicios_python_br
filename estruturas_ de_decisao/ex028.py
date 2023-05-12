# 28.O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#  File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#  Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#  Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#  Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de #  carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("======== Hipermercado Tabajara =======")

tipo_carne = input('Digite o tipo de carne desejado (File Duplo, Alcatra ou Picanha): ').upper().strip()
quantidade = float(input('Digite a quantidade em Kg: ').strip())
cartao_tabajara = input('A compra será realizada com o cartão Tabajara? (S/N): ').upper().strip()

if cartao_tabajara == 'S':

    if quantidade <= 5:
        if tipo_carne == 'FILE DUPLO':
            preco_total = quantidade * 4.9
        elif tipo_carne == 'ALCATARA':
            preco_total = quantidade * 5.9
        elif tipo_carne == 'PICANHA':
            preco_total = quantidade * 6.9

    else:
        if tipo_carne == 'FILE DUPLO':
            preco_total = quantidade * 5.8
        elif tipo_carne == 'ALCATARA':
            preco_total = quantidade * 6.8
        elif tipo_carne == 'PICANHA':
            preco_total = quantidade * 7.8

    tipo_pagamento = 'cartão'
    desconto = preco_total * 0.05
    valor_a_pagar = preco_total - desconto

if cartao_tabajara == 'N':

    if quantidade <= 5:
        if tipo_carne == 'FILE DUPLO':
            preco_total = quantidade * 4.9
        elif tipo_carne == 'ALCATARA':
            preco_total = quantidade * 5.9
        elif tipo_carne == 'PICANHA':
            preco_total = quantidade * 6.9

    else:
        if tipo_carne == 'FILE DUPLO':
            preco_total = quantidade * 5.8
        elif tipo_carne == 'ALCATARA':
            preco_total = quantidade * 6.8
        elif tipo_carne == 'PICANHA':
            preco_total = quantidade * 7.8

    tipo_pagamento = 'dinheiro'
    desconto = 0
    valor_a_pagar = preco_total - desconto

print("-------- Cupom Fiscal --------")
print("Tipo de carne:", tipo_carne)
print("Quantidade:", quantidade, "Kg")
print("Preço total: R$", preco_total)
print("Tipo de pagamento:", tipo_pagamento)
print("Valor do desconto: R$", desconto)
print("Valor a pagar: R$", valor_a_pagar)