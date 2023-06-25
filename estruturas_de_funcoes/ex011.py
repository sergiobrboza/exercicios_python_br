# 11.Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
def data_por_extenso(data):
    dia, mes, ano = data.split('/')

    if not validar_data(int(dia), int(mes), int(ano)):
        return 'NULL'
    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'
    }
    data_extenso = f'{int(dia)} de {meses[int(mes)]} de {ano}'

    return data_extenso

def validar_data(dia, mes, ano):
    if dia > 31 or dia < 1 or mes < 1 or mes > 12 or ano < 1:
        return False
    elif mes == 2:
        if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia > 29:
                return False
        elif dia > 28:
            return False
    return True

data = input('Digite a data no formato DD/MM/AAAA: ')
data_extenso = data_por_extenso(data)
print(data_extenso)