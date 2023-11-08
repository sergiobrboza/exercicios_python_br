# 3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: Feminino - Masculino

while True:
    genero = str(input('Digite F para feminino e M para masculino: ').upper().strip())

    masculino = (genero == 'M')
    feminino = (genero == 'F')

    if  genero == 'M' or genero == 'F':
        resultado = 'Feminino' if feminino else 'Masculino'
        print(f'{resultado}')
        break
    else:
        resultado = 'Digite M ou F'
        print(f'{resultado}')
