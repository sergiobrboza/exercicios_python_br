# 4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vetor = []
consoantes = 0

for i in range(10):
    caractere = input("Digite um caractere: ")
    vetor.append(caractere)

    if caractere.lower() not in ['a', 'e', 'i', 'o', 'u']:
        consoantes += 1

print("Consoantes lidas:", consoantes)
print("Consoantes encontradas:")

for caractere in vetor:
    if caractere.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(caractere, end=' -> ')
