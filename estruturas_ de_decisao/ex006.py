# 6.Faça um Programa que leia três números e mostre o maior deles.

numeros = {}

for indice in range(3):
    num = float(input('Digite o número: '))
    numeros[indice] = num

maior = max(numeros)

    
print(f'O maior número é o {maior}')
