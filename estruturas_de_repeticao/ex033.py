# 33.O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
temperaturas = []
cont_temp = 0
while True:
    temp = float(input('Digite a temperatura em C°: '))
    cont_temp += 1
    continua = input('Para parar digite N, para continuar digite qualquer coisa: ')
    temperaturas.append(temp)
    if continua == 'N':
        temp_maior = max(temperaturas)
        temp_menor = min(temperaturas)
        temp_media = sum(temperaturas) / cont_temp
        break
print(f'A maior temperatura é {temp_maior}C°')
print(f'A menor temperatura é {temp_menor}C°')
print('E a temperatura média é de {:.2f}C°'.format(temp_media))