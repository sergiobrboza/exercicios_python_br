# 21.Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#  a.Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#  b.Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


saque = int(input('Digite quanto deseja sacar: '))

if saque >= 600:
    print("Seu limite é de R$600,00!")
elif saque < 10:
    print('O saque minimo é de R$10,00!')
else:
    notas_100 = saque // 100
    notas_50 = (saque % 100) // 50
    notas_10 = (saque % 50) // 10
    notas_5 = (saque % 10) // 5
    notas_1 = (saque % 5)
    
    print(f"Notas de R$ 100: {notas_100}")
    print(f"Notas de R$ 50: {notas_50}")
    print(f"Notas de R$ 10: {notas_10}")
    print(f"Notas de R$ 5: {notas_5}")
    print(f"Notas de R$ 1: {notas_1}")