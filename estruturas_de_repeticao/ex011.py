# 11.Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
num1 += 1
soma = 0
for num in range(num1, num2):
    soma += num
print('O resultado é: ',soma)