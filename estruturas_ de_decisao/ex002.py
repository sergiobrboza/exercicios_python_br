# 2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def verifica():
    valor = float(input('Digite um numero positivo ou negativo: '))

    if valor != 0:
        resultado = 'Positivo' if valor > 0 else 'Negativo'
    else:
        resultado = 'Neutro'
    print(f'O número é {resultado}')

verifica()
