# 2.Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ' '.join(str(j) for j in range(1, i + 1))
        print(linha)
n = int(input('Digite um número inteiro: '))
imprimir_padrao(n)