# 11.Altere o programa anterior, intercalando 3 vetores de 10 elementos cada
vetor1 = []
vetor2 = []
vetor3 = []

for a in range (10):
    num = int(input(f'Informe o {a + 1}° elemento do 1° vetor: '))
    vetor1.append(num)

for b in range(10):
    num = int(input(f'Informe o {b + 1}° elemento do 2° vetor: '))
    vetor2.append(num)

for c in range(10):
    num = int(input(f'Informe o {c + 1}° elemento do 3° vetor: '))
    vetor3.append(num)

vetor4 = []

for d in range(10):
    vetor4.append(vetor1[d])
    vetor4.append(vetor2[d])
    vetor4.append(vetor3[d])
print(f'A junção dos três vetores ficou assim {vetor4}')