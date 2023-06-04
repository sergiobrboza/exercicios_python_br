# 8.Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
alturas = []
idades = []
for p in range(5):
    alt = float(input('Altura em cm: '))
    id = int(input('Idade: '))
    alturas.append(alt)
    idades.append(id)

print("Idades na ordem inversa:")
for idade in reversed(idades):
    print(idade, end=' ')

print("Alturas na ordem inversa:")
for altura in reversed(alturas):
    print(altura, end=' ')