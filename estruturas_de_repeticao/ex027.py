# 27.Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
qtd_turmas = int(input('Digite a quantidade de turmas: '))
qtd_alunos = []
for i in range(qtd_turmas):
    alunos = float(input('Digite quantos alunos tem a turma {}: '.format(i+1)))
    if alunos > 40:
        print('As turmas não podem ter mais do que 40 alunos, Faça novamente.')
        break
    qtd_alunos.append(alunos)
    resultado = sum(qtd_alunos) / qtd_turmas
else:
    print('A média de alunos é de:',resultado)    