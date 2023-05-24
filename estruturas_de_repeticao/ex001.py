# 1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input('Digite a nota de 0 á 10: '))
    if nota <= 10:
        print('A nota informada foi: ',nota)
        break