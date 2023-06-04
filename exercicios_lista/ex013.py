# 13.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp = []
for mes in meses:
    media_mes= float(input(f'Digite a temperatura media do mês de {mes} em C°: '))
    temp.append(media_mes)

media_anual = sum(temp) / len(temp)

print(f'Temperaturas acima da média anual: de {media_anual}C°')
for t in range(len(meses)):
    if temp[t] > media_anual:
        print(f'{meses[t]}: {temp[t]}C°')