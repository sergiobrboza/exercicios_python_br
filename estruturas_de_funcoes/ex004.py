# 4.Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def testa_positivo(n):
    if n <= 0 :
        return 'N'
    else:
        return 'P'
n = float(input('Digite qualquer número: '))
teste = testa_positivo(n)
print(f'O número {n} é {teste}')