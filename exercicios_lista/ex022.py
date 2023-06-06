# 22.Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%
situacoes = {
    1: "necessita da esfera",
    2: "necessita de limpeza",
    3: "necessita troca do cabo ou conector",
    4: "quebrado ou inutilizado"
}

quantidades = {situacao: 0 for situacao in situacoes.values()}

while True:
    identificacao = int(input("Número de identificação do mouse (0 para encerrar): "))
    if identificacao == 0:
        break

    print("Situações:")
    for codigo, situacao in situacoes.items():
        print(f"{codigo} - {situacao}")

    defeito = int(input("Tipo de defeito: "))

    if defeito in situacoes:
        quantidades[situacoes[defeito]] += 1
    else:
        print("Defeito inválido. Mouse não será considerado.")

quantidade_total = sum(quantidades.values())

print("\nRelatório:")
print(f"Quantidade de mouses: {quantidade_total}\n")
print("Situação                        Quantidade              Percentual")
for codigo, situacao in situacoes.items():
    quantidade = quantidades[situacao]
    percentual = (quantidade / quantidade_total) * 100
    print(f"{codigo}- {situacao:30} {quantidade:15} {percentual:10.2f}%")
