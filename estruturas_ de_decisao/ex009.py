# 9.Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

lista_ordenada = sorted([num1, num2, num3])

print("Os números em ordem decrescente são:\n", lista_ordenada[2], lista_ordenada[1], lista_ordenada[0])