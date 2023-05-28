# 37.Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
def calcular_estatisticas(clientes):
    codigo_mais_alto = codigo_mais_baixo = codigo_mais_gordo = codigo_mais_magro = ''
    altura_mais_alto = altura_mais_baixo = peso_mais_gordo = peso_mais_magro = 0
    soma_alturas = soma_pesos = 0

    for cliente in clientes:
        codigo, altura, peso = cliente

        if altura > altura_mais_alto:
            codigo_mais_alto = codigo
            altura_mais_alto = altura

        if altura < altura_mais_baixo or altura_mais_baixo == 0:
            codigo_mais_baixo = codigo
            altura_mais_baixo = altura

        if peso > peso_mais_gordo:
            codigo_mais_gordo = codigo
            peso_mais_gordo = peso

        if peso < peso_mais_magro or peso_mais_magro == 0:
            codigo_mais_magro = codigo
            peso_mais_magro = peso

        soma_alturas += altura
        soma_pesos += peso

    media_alturas = soma_alturas / len(clientes)
    media_pesos = soma_pesos / len(clientes)

    return (codigo_mais_alto, altura_mais_alto, codigo_mais_baixo, altura_mais_baixo,
            codigo_mais_gordo, peso_mais_gordo, codigo_mais_magro, peso_mais_magro,
            media_alturas, media_pesos)

clientes = []

while True:
    codigo = input("Digite o código do cliente (ou 0 para sair): ")
    if codigo == '0':
        break

    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))

    clientes.append((codigo, altura, peso))

resultado = calcular_estatisticas(clientes)

print("\nResultados:")
print("Cliente mais alto:")
print("Código:", resultado[0])
print("Altura:", resultado[1])

print("\nCliente mais baixo:")
print("Código:", resultado[2])
print("Altura:", resultado[3])

print("\nCliente mais gordo:")
print("Código:", resultado[4])
print("Peso:", resultado[5])

print("\nCliente mais magro:")
print("Código:", resultado[6])
print("Peso:", resultado[7])

print("\nMédia das alturas:", resultado[8])
print("Média dos pesos:", resultado[9])