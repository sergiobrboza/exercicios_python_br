# 17.Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
saltos = []
while True:
    nome = input('Digite o nome do atleta, O programa para caso digite nada: ')
    if nome == '':
        break
    for s in range(1,6):
        salt = float(input(f'{s}° Salto:'))
        saltos.append(salt)
    media = sum(saltos) / 5
    print('-=' * 30)
    print('Resultado Final:')
    print('Atleta:', nome)
    print('Saltos:', ' - '.join(map(str,saltos)))
    print('Média dos Saltos:', media, 'm\n')