# 3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = str(input('Digite F para feminino e M para masculino: ').upper().strip())

if genero == 'M':
    print('Masculino')
elif genero == 'F':
    print('Feminino')
else:
    print('Sexo invalido')
