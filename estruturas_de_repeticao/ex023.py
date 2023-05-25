# 23.Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
def contar_divisoes(numero):
    count = 0
    for i in range(2, int(numero ** 0.5) + 1):
        count += 1
        if numero % i == 0:
            return count
    return count
def encontrar_primos(n):
    primos = []
    divisores_totais = 0
    for num in range(2, n + 1):
        divisoes = contar_divisoes(num)
        divisores_totais += divisoes
        if divisoes == 0:
            primos.append(num)
    return primos, divisores_totais
n = int(input("Digite um número inteiro: "))

primos, divisoes_totais = encontrar_primos(n)

print("Números primos entre 1 e", n, ":")
print(primos)
print("Número total de divisões:", divisoes_totais)