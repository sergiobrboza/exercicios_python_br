# 15.Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
notas = []
while True:
    nt = float(input('Digite as notas, caso queira parar o programa digite -1:'))
    if nt != -1:
        notas.append(nt)
    else:
        break

soma = sum(notas)
media = sum(notas) / len(notas)

cont_acima = cont_abaixo = 0
for elemento in notas:
        if elemento > media:
            cont_acima += 1
        if elemento < media:
             cont_abaixo += 1

print('-=' * 30)
print(f'O resultado da soma dos valores é de: {soma}')
print(f'A média dos valores é de: {media}')
print(f'{cont_acima} números estam acima da média')
print(f'{cont_abaixo} números estam abaixo da média')
print('-=' * 30)
print('Obrigado pela a confiança')