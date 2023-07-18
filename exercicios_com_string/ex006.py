# 6.Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.

from datetime import datetime

def data_extenso(data_str):
    meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        dia = data.day
        mes = meses[data.month]
        ano = data.year

        print(f"Você nasceu em {dia} de {mes} de {ano}.")
    except ValueError:
        print("Data de nascimento inválida. Certifique-se de usar o formato dd/mm/aaaa.")

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_extenso(data_nascimento)
