# 4.Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

def vertical_name_ladder(Name):
    Name_accumulated = ''

    for letter in Name:
        Name_accumulated += letter
        print(Name_accumulated)

name_user = input('Digite seu nome: ')
vertical_name_ladder(name_user.upper())