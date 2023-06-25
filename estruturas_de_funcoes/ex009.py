# 9.Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso_numero(numero):
    num_str = str(numero)
    reverso_str = num_str[::-1]
    reverso = int(reverso_str)
    return reverso

numero = int(input('Digite um número inteiro: '))
reverso = reverso_numero(numero)
print(f'O número {numero} ao contrario {reverso}')