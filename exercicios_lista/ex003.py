# 3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for num in range(1, 5):
    valor = float(input(f'Digite o {num}° número: '))
    notas.append(valor)
media = sum(notas) / num
print(f'As notas foram: {notas}')
print(f'A media do aluno foi de {media}.')