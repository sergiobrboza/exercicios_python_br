# 1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
lista = list()
for num in range(1, 6):
    num = int(input(f'Digite o {num}° número: '))
    lista.append(num)
print(f'Os número digitado foram: {lista}')