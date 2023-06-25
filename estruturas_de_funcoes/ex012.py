# 12.Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
from random import shuffle

def embaralhar_palavra(palavra):
    caracteres = list(palavra)

    shuffle(caracteres)
    palavra_embaralhada = ''.join(caracteres)

    return palavra_embaralhada.upper()

palavra = input('Digite uma palavra: ')
palavra_embaralhada = embaralhar_palavra(palavra)
print('Palavra embaralhada:',palavra_embaralhada)