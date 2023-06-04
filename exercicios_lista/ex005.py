# 5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
vetor = []
par = []
impar = []
for i in range(1, 21):
    num = int(input(f'Digite o {i}° número: '))
    vetor.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
vetor.sort()
par.sort()
impar.sort()
print(f'Você digitou os números: {vetor}')
print(f'Desses números, esses são os pares: {par}')
print(f'E esses são os ímpares: {impar}')