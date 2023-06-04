# 9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
vetor_a = []
for i in range(10):
    num = int(input('Digite o valor: '))
    vetor_a.append(num)

soma_quadrados = 0
for num in vetor_a:
    soma_quadrados += num ** 2
print(f'O resultado da soma dos números elevados ao quadrado é de {soma_quadrados}')