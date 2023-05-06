# 11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

inum1 = int(input('Dgite algum numero inteiro: '))
inum2 = int(input('Digite outro numero inteiro: '))
rnum = float('Digite um numero real: ')

print('a. {}'.format(inum1 * 2 + inum2 / 2))
print('b. {}'.format(inum1 * 3 + rnum))
print('c. {}'.format(rnum ** 3))