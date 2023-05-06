# 10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = int(input('Transforme C° em F°: '))
print('{}C° é o equivalente a {:.2f}F°'.format(celsius, (celsius * 9 / 5) + 32))