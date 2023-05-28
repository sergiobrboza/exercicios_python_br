# 40.Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# a.Código da cidade;
# b.Número de veículos de passeio (em 1999);
# c.Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e.Qual a média de veículos nas cinco cidades juntas;
# f.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
num_cidades = 5
maior_indice_acidentes = menor_indice_acidentes = 0
cidade_maior_indice = cidade_menor_indice = ''
soma_veiculos = 0
soma_acidentes_menos_2000 = 0
count_cidades_menos_2000 = 0

for i in range(num_cidades):
    codigo_cidade = input("Digite o código da cidade: ")
    num_veiculos = int(input("Digite o número de veículos de passeio (em 1999): "))
    num_acidentes = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))

    if i == 0:
        maior_indice_acidentes = menor_indice_acidentes = num_acidentes
        cidade_maior_indice = cidade_menor_indice = codigo_cidade
    else:
        if num_acidentes > maior_indice_acidentes:
            maior_indice_acidentes = num_acidentes
            cidade_maior_indice = codigo_cidade
        if num_acidentes < menor_indice_acidentes:
            menor_indice_acidentes = num_acidentes
            cidade_menor_indice = codigo_cidade

    soma_veiculos += num_veiculos

    if num_veiculos < 2000:
        soma_acidentes_menos_2000 += num_acidentes
        count_cidades_menos_2000 += 1

media_veiculos = soma_veiculos / num_cidades
media_acidentes_menos_2000 = soma_acidentes_menos_2000 / count_cidades_menos_2000

print("\nEstatísticas:")
print("Maior índice de acidentes de trânsito:", maior_indice_acidentes, "- Cidade:", cidade_maior_indice)
print("Menor índice de acidentes de trânsito:", menor_indice_acidentes, "- Cidade:", cidade_menor_indice)
print("Média de veículos nas cinco cidades:", media_veiculos)
print("Média de acidentes de trânsito nas cidades com menos de 2000 veículos:", media_acidentes_menos_2000)
