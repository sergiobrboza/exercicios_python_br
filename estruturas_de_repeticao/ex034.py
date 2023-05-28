# 34.Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
def encontra_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
if encontra_primo(num):
    print('Esse número é um número primo')
else:
    print('Esse número não é um número primo')