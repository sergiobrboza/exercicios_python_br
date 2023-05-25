# 19.Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
numeros = []
num = int(input('Digite a quantidade de números no conjunto: '))

for i in range(num):
    numero = float(input('Digite um número: '))
    if numero > 1000 or numero <= 0:
        print('Não é possivel utilizar números maiores que 1000 ou menores que 0.')
        break
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)
print('O maior valor é', maior)
print('O menor valor é', menor)
print('O resultado da soma dos valores é', soma)