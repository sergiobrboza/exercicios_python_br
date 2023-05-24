# 8.Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for i in range (5):
    num = float(input('Digite o valor: '))
    soma += num
    resultado = soma / 5
print('A media entre os numeros informados é de: ', resultado)