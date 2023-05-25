# 22.Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
def encontrar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_divisores(numero):
    divisores = []
    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

num = int(input("Digite um número: "))

if encontrar_primo(num):
    print(num, "é um número primo.")
else:
    print(num, "não é um número primo.")
    divisores = encontrar_divisores(num)
    print("É divisível por:", divisores)