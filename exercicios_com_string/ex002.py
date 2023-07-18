# 2.Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

def string_reverse(texto):
    return texto[::-1]

# Exemplo de uso
Name = input('Digite seu nome (pode usar letras maicúla e minúsculas): ')
string_invertida = string_reverse(Name)

print("String Original:", Name)
print("String Invertida:", string_invertida.upper())
