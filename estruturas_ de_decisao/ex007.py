# 7.Faça um Programa que leia três números e mostre o maior e o menor deles.
numeros = {}

for indice in range(3):
    num = float(input('Digite o número: '))
    numeros[indice] = num

id_menor = min(numeros, key=numeros.get)
menor_num = numeros[id_menor]

id_maior = max(numeros, key=numeros.get)
maior_num = numeros[id_maior]
    
print(f'O maior número é o {maior_num} e o menor número é o {menor_num}')
