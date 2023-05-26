# 25.Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
qtd_pessoas = int(input('Digite a quantidade de pessoas: '))
idade = []
for i in range(qtd_pessoas):
    valor = float(input('Digite a idade {}: '.format(i+1)))
    idade.append(valor)
media = sum(idade) / qtd_pessoas
if media < 25:
    print(f'A media de idade é de {media}, significa que a maioria são jovens')
elif media > 26 and media < 60:
    print(f'A media de idade é de {media}, significa que a maioria são adultos')
else:
    print(f'A media de idade é de {media}, significa que a maioria são idosos')