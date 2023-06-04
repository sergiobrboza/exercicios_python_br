# 2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = list()
for num in range(1, 11):
    num = float(input(f'Digite o {num}° número: '))
    lista.append(num)
    lista.sort(reverse = True)
print(f'Os número digitado foram: {lista}')