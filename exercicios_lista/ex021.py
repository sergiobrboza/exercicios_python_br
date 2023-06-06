# 21.Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# A.O modelo do carro mais econômico;
# B.Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
# Comparativo de Consumo de Combustível

# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5

# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.
modelos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeout"]
consumo = [7, 10, 12.5, 9, 14.5]

litros_1000km = [1000 / km for km in consumo]
preco_gasolina = 2.25
custo_1000km = [litros * preco_gasolina for litros in litros_1000km]

indice_menor_consumo = consumo.index(min(consumo))

print("Comparativo de Consumo de Combustível\n")

for i in range(len(modelos)):
    print(f"Veículo {i+1}")
    print(f"Nome: {modelos[i]}")
    print(f"Km por litro: {consumo[i]}")
    print()

print("Relatório Final")
for i in range(len(modelos)):
    print(f"{i+1} - {modelos[i]} - {consumo[i]:4.1f} - {litros_1000km[i]:6.1f} litros - R$ {custo_1000km[i]:.2f}")

print(f"\nO menor consumo é do {modelos[indice_menor_consumo]}.")
