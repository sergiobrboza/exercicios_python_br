# 4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

while True:
    entrada = input("Digite uma letra: ")
    vogal = (entrada.lower() in 'aeiou')
    
    if len(entrada) == 1 and not entrada.isnumeric():
        resultado = 'VOGAL' if vogal else 'CONSOANTE'
        print(f'A letra {entrada.upper()} é uma {resultado}')
        break
    else:
        print("Por favor, digite apenas uma letra.")
