#7.Faça um programa que leia 5 números e informe o maior número.
maior = None
for i in range (5):
    num = float(input('Digite um valor: '))
    if maior is None or maior < num:
        maior = num
print('O maior numero é: ', maior)