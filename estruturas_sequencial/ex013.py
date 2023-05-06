# 13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7

alturah = float(input('Para saber o seu peso ideal de um homem. Digite sua altura: '))
alturam = float(input('Para saber o seu peso ideal de uma mulher. Digite sua altura: '))

print('a. O seu peso ideal sendo homem é de: {}'.format((72.7 * alturah) - 58))
print('b. O seu peso ideal sendo mulher é de: {}'.format((62.1 * alturam) - 44.7))