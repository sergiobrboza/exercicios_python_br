# 3.Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

# F
# U
# L
# A
# N
# O

def vertical_name(Name):
    for letter in Name:
        print(letter)

name_user = input('Digite seu nome: ')
vertical_name(name_user.upper())