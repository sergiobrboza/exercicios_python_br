# 16.Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
contadores = [0] * 9

while True:
    vendas_brutas = float(input("Informe as vendas brutas do vendedor (ou -1 para encerrar): "))
    
    if vendas_brutas == -1:
        break
    
    salario = 200 + 0.09 * vendas_brutas
    
    posicao = int((salario - 200) // 100)
    
    if posicao < 9:
        contadores[posicao] += 1
    else:
        contadores[8] += 1

faixas_salariais = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
                    "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]

for i in range(9):
    print(f"{faixas_salariais[i]}: {contadores[i]}")

