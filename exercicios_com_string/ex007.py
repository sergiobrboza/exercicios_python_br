# 7.Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# A.quantos espaços em branco existem na frase.
# B.quantas vezes aparecem as vogais a, e, i, o, u.
def contar_espacos_e_vogais(frase):
 
    espacos = 0
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for letra in frase:

        if letra == ' ':
            espacos += 1

        elif letra.lower() in vogais:
            vogais[letra.lower()] += 1

    return espacos, vogais

frase_usuario = input("Digite uma frase: ")

espacos, vogais = contar_espacos_e_vogais(frase_usuario)

print("A. Quantidade de espaços em branco:", espacos)
print("B. Quantidade de vezes que aparecem as vogais:")
for vogal, quantidade in vogais.items():
    print(f"{vogal}: {quantidade}")
