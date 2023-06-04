# 12.Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = []
alturas = []

for a in range(3):
    id = int(input(f'Digite a {a + 1}° idade: '))
    alt = int(input(f'Digite a {a + 1}° altura: '))
    idades.append(id)
    alturas.append(alt)

media = sum(alturas) / len(alturas)

inferior_media = 0
for b in range(3):
    if idades[b] >= 13 and alturas[b] <= media:
        inferior_media += 1

print(f'{inferior_media} dos alunos são inferiores a média')