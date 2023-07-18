# 5.Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F
def vertical_name_ladder(Name):
    tamanho = len(Name)
    for i in range(tamanho, 0, -1):
        print(Name[:i])

user_name = input("Digite seu nome: ")
vertical_name_ladder(user_name)
