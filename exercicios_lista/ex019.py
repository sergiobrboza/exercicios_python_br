# 19.Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
sistemas = [0] * 7
nomes = [['Windows Server'], ['Unix'], ['Linux'], ['Netware'], ['Mac Os'], ['Outro']] * 7

while True:
    print('Sistemas Operacionais: \n1- Windows Server \n2-Unix \n3-Linux \n4-Netware \n5-Mac Os \n6-Outro')
    voto = int(input('Qual o melhor Sistema Operacional para uso em servidores? (Ou 0 para encerrar): '))
    if voto == 0:
        break
    if voto < 1 or voto > 6:
        print('Voto invalido. Informe um valor de 1 a 6.')
        continue
    sistemas[voto] += 1
total_votos = sum(sistemas)
print("\nSistema Operacional     Votos   %")
print("-------------------     -----   ---")
for i in range(1,7):
    percentual = (sistemas[i] / total_votos) * 100
    print(f"{i}-{''.join(map(str,nomes[i]))} {' '*(23-len(str(i)))} {sistemas[i]}   {percentual:.0f}%")

print("-------------------     -----   ---")
print(f"Total                    {total_votos}\n")   
vencedor = sistemas.index(max(sistemas[1:]))
votos_vencedor = sistemas[vencedor]
percentual_vencedor = (votos_vencedor / total_votos) * 100

print(f"O Sistema Operacional mais votado foi o {vencedor}, com {votos_vencedor} votos, correspondendo a {percentual_vencedor:.0f}% dos votos.") 