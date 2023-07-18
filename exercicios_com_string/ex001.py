# 1.Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

def main():

    string1 = input('Digite a primeira frase: ')
    string2 = input('Digite a segunda frase: ')

    len_string1 = len(string1)
    len_string2 = len(string2)

    same_length = len_string1 == len_string2

    same_content = string1 == string2

    print("\nConteúdo e comprimento das strings:")
    print(f"String 1: {string1}, Comprimento: {len_string1}")
    print(f"String 2: {string2}, Comprimento: {len_string2}")

    if same_length:
        if same_content:
            print('AS duas strings são de tamanhos iguais ')
            print('As duas strings possuem o mesmo conteúdo')
        else:
            print('AS duas strings são de tamanhos iguais')
            print('As duas strings possuem conteúdos diferentes')
    else:
        if same_content:
            print('As duas strings são de tamanhos diferentes')
            print('As duas strings possuem o mesmo conteúdo')
        else:
            print('As duas strings são de tamanhos diferentes')
            print('As duas strings possuem conteúdos diferentes')

if __name__ =="__main__":
    main()
    