# 39.Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
num_aluno_mais_alto = num_aluno_mais_baixo = 0
altura_mais_alto = altura_mais_baixo = 0

for i in range(1, 11):
    num_aluno = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno em centímetros: "))

    if altura > altura_mais_alto or i == 1:
        num_aluno_mais_alto = num_aluno
        altura_mais_alto = altura

    if altura < altura_mais_baixo or i == 1:
        num_aluno_mais_baixo = num_aluno
        altura_mais_baixo = altura

print("Aluno mais alto:")
print("Número do aluno:", num_aluno_mais_alto)
print("Altura:", altura_mais_alto, "cm")

print("\nAluno mais baixo:")
print("Número do aluno:", num_aluno_mais_baixo)
print("Altura:", altura_mais_baixo, "cm")
