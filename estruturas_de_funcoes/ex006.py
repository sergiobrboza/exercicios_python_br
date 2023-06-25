# 6.Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def converter_hora(horas, minutos):
    if horas == 0:
        horas = 12
        periodo = 'A.M'
    elif horas < 12:
        periodo = 'A.M'
    elif horas == 12:
        periodo = 'P.M'
    else:
        horas -= 12
        periodo = 'P.M'
    return horas, minutos, periodo

def exibir_hora(horas, minutos, periodo):
    print(f'A hora convertida é : {horas}:{minutos} {periodo}')

while True:
    horas = int(input('Digite as horas (0-23): '))
    minutos = int(input('Digite os minutos (0-59): '))
    
    horas_convertidas, minutos_convertidos, periodo = converter_hora(horas, minutos)
    exibir_hora(horas_convertidas, minutos_convertidos, periodo)

    opcao = input('Deseja converter outra hora? (S/N) ')
    if opcao.upper() != 'S':
        break