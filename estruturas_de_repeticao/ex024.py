# 24.Faça um programa que calcule o mostre a média aritmética de N notas.
qtd_notas = int(input('Digite a quantidade de notas: '))
notas = []
for i in range(qtd_notas):
    valor = float(input('Digite o valor da nota {}: '.format(i+1)))
    notas.append(valor)
resultado = sum(notas) / qtd_notas
print(resultado)