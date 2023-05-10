# 18.Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int, data.split('/'))

if ano <= 0 or ano > 9999:
    print("Data inválida.")
    exit()

if mes < 1 or mes > 12:
    print("Data inválida.")
    exit()

dias_por_mes = [31, 28 if ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if dia < 1 or dia > dias_por_mes[mes-1]:
    print("Data inválida.")
    exit()

print("Data válida.")