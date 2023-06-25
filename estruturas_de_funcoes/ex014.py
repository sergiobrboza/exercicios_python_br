# 14.Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

# 8  3  4 
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
import itertools

def encontrar_quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quadrados_magicos = []

    permutacoes = itertools.permutations(numeros)

    for permutacao in permutacoes:
        linha1 = permutacao[0:3]
        linha2 = permutacao[3:6]
        linha3 = permutacao[6:9]

        if sum(linha1) == sum(linha2) == sum(linha3) == linha1[0] + linha2[0] + linha3[0] == linha1[1] + linha2[1] + linha3[1] == linha1[2] + linha2[2] + linha3[2] == linha1[0] + linha2[1] + linha3[2] == linha1[2] + linha2[1] + linha3[0]:
            quadrado_magico = [linha1, linha2, linha3]
            quadrados_magicos.append(quadrado_magico)

    for quadrado_magico in quadrados_magicos:
        for linha in quadrado_magico:
            print(' '.join(str(num) for num in linha))
        print()

encontrar_quadrados_magicos()
