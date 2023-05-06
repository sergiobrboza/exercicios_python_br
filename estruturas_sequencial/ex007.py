# 7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quadrado = int(input('Qual é o tamanho de um dos lados do quadrado? '))
area = quadrado**2

print('A área desse quadrado é de {}, e o seu dobro é de {}'.format(area, area * 2))