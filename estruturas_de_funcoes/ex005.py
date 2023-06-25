# 5.Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImpost, custo):
    imposto = custo * taxaImpost / 100
    custo += imposto
    return custo

valor_item = 100
taxa = 10
valor_final = somaImposto(taxa, valor_item)
print(f'O valor final do item, incluindo os impostos ja pré definidos, é de R$ {valor_final}.')