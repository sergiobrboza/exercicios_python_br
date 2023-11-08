# 1.Faça um Programa que peça dois números e imprima o maior deles.

numeros = {}
for indice in range(1,3):
    num = float(input(f'Digite o {indice}° número: '))
    numeros[indice] = num

maior = max(numeros)
print(f'O maior número é o {maior}')