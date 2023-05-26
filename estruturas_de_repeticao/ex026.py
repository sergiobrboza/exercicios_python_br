# 26.Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
qtd_pessoas = int(input('Digite a quantidade de eleitores: '))
bolsonaro = lula = ciro = nulo = 0
for i in range(qtd_pessoas):
    voto = float(input('Candidatos a eleiçâo \n[ 22 ] Bolsonaro \n[ 13 ] Lula \n[ 12 ] Ciro \n[ 0 ] Nulo \nEleitor {} digite seu voto: '.format(i+1)))
    if voto == 22:
        bolsonaro += 1
    elif voto == 13:
        lula += 1
    elif voto == 12:
        ciro += 1
    elif voto == 0:
        nulo +=1
print(f'Bolsonaro teve: {bolsonaro} votos')
print(f'Lula teve: {lula} votos')
print(f'Ciro teve: {ciro} votos')
print(f'Votos nulos: {nulo}')