# 28.Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
qtd_cds = int(input('Digite a quantidade de CDs: '))
cds = []
for i in range(qtd_cds):
    valor = float(input('Digite o valor gasto no CD {}: '.format(i+1)))
    cds.append(valor)
total_gasto = sum(cds)
media = total_gasto / qtd_cds
print(f'O colecionador gastou R${total_gasto} e a media que ele gatou por CD é de R${media}')