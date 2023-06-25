# 8.Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def conta_num(num):
    num_str = str(num)
    quantidade_dig = len(num_str)
    return quantidade_dig
num = int(input('Informe um número inteiro: '))
quantidade = conta_num(num)
print(f'O número {num} tem {quantidade} dígitos')