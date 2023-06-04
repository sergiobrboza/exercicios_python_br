# 6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias_alunos = []
cont = 0
for aluno in range(1,11):
    notas = []
    print(f'Digite as notas do {aluno}° aluno')
    for i in range(1, 5):
        nota = float(input(f'Digite a {i}° nota: '))
        notas.append(nota)

    media = sum(notas) / 4
    medias_alunos.append(media)

    if media >= 7:
        cont += 1
print(f'Foram {cont} que tiraram acima ou igual a nota 7.0')