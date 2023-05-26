# 32.Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120
def calcular_fatorial(numero):
    fatorial = 0
    for i in range(2, numero + 1):
        fatorial *= i
    return fatorial
num = int(input('Fatorial de: '))
resultado = calcular_fatorial(num)

print('{}! = '.format(num), end='')
for i in range(num, 1,-1):
    print(i, end=' . ')
print('1 =', resultado)