# 21.Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int(input('Digite um número inteiro: '))
def verifica_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
if verifica_primo(num):
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')