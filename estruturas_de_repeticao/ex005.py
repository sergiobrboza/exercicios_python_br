# 5.Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
while True:
    try:
        populacao_a = int(input("Informe a população do país A: "))
        taxa_crescimento_a = float(input("Informe a taxa de crescimento do país A (em decimal): "))
        populacao_b = int(input("Informe a população do país B: "))
        taxa_crescimento_b = float(input("Informe a taxa de crescimento do país B (em decimal): "))

        if populacao_a <= 0 or populacao_b <= 0 or taxa_crescimento_a < 0 or taxa_crescimento_b < 0:
            print("Valores inválidos. As populações devem ser maiores que zero e as taxas de crescimento não podem ser negativas.")
            continue

        anos = 0

        while populacao_a < populacao_b:
            populacao_a += populacao_a * taxa_crescimento_a
            populacao_b += populacao_b * taxa_crescimento_b
            anos += 1

        print("Serão necessários", anos, "anos para a população do país A ultrapassar ou igualar a população do país B.")
        break

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números inteiros para as populações e números decimais para as taxas de crescimento.")

    resposta = input("Deseja realizar outra operação? (S/N): ")
    if resposta.upper() != "S":
        break
