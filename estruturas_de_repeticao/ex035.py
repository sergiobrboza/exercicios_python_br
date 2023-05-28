# 35.Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def gerar_primos(N):
    primos = []
    for num in range(2, N + 1):
        if verificar_primo(num):
            primos.append(num)
    return primos

N = int(input("Digite um número inteiro: "))

primos = gerar_primos(N)

print("Números primos entre 1 e", N, ":")
print(primos)
