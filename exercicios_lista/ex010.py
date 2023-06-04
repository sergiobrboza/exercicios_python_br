# 10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetor1 = []
vetor2 = []

for a in range (10):
    num = int(input(f'Informe o {a + 1}° elemento: '))
    vetor1.append(num)

for b in range(10):
    num = int(input(f'Informe o {b + 1}° elemento: '))
    vetor2.append(num)

vetor3 = []
for c in range(10):
    vetor3.append(vetor1[c])
    vetor3.append(vetor2[c])
print(f'A junção do primeiro vetor com o segundo ficou assim {vetor3}')