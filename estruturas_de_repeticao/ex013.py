# 13.Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
print('Base ^ expoente:')
base = int(input('Base: '))
expoente = int(input('Expoente: '))

potencia = 1
count = 1

while count <= expoente:
    potencia *= base
    count +=1
print(base, '^', expoente, '=', potencia)