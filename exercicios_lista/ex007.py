# 7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor = []

for i in range(5):
    numero = int(input(f"Informe o número {i+1}: "))
    vetor.append(numero)

soma = sum(vetor)
multiplicacao = 1
for numero in vetor:
    multiplicacao *= numero

print("Números informados:", vetor)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
