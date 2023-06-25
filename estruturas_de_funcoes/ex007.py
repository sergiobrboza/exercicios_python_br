# 7.Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def valorPagamento(valorPrestacao, diasAtraso):
    if diasAtraso == 0:
        return valorPrestacao
    else:
        multa = valorPrestacao* 0.03
        juros = valorPrestacao * (0.001 * diasAtraso)
        return valorPrestacao + multa+ juros
    
totalPrestacoes = 0
totalValorPago = 0

while True:

    valor = float(input('Digite o valor da prestacão(ou 0 para sair): '))
    
    if valor == 0:
        break

    diasAtraso = int(input('Digite quantos dias em atraso: '))

    valorPagar = valorPagamento(valor,diasAtraso)
    
    totalPrestacoes += 1
    totalValorPago += valorPagar
    print(f'Valor a ser pago: R${valorPagar:.2f}\n')

print('\nRelatório do dia: ')
print(f'Quantidade de prestações pagas: {totalPrestacoes}')
print(f'Valor total recebido: R${totalValorPago:.2f}')