# 9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 

fahrenheit = int(input('Transforme F° em C°: '))
print('{}F° é o equivalente a {:.2f}C°'.format(fahrenheit, (fahrenheit - 32) * 5 / 9 ))