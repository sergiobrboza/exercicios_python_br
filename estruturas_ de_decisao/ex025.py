# 25.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#  a."Telefonou para a vítima?"
#  b."Esteve no local do crime?"
#  c."Mora perto da vítima?"
#  d."Devia para a vítima?"
#  e."Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print('Digite o numero [ 1 ] para SIM ou [ 0 ] para NÃO')

info1 = int(input('Telefonou para a vitima? '))
info2 = int(input('Esteve no local do crime?'))
info3 = int(input('Mora perto da vitima? '))
info4 = int(input('Devia a vitima? '))
info5 = int(input('Ja trabalhou com a vitima? '))

resultado = info1 + info2 + info3 + info4 + info5

if resultado < 2:
    print('Você é inocente')
elif resultado == 2:
    print('Você é suspeito')
elif resultado >= 3 and resultado <= 4:
    print('Você é cumplice')
else:
    print('Você é o assassino')
