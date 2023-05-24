# 3.Faça um programa que leia e valide as seguintes informações:
# a.Nome: maior que 3 caracteres;
# b.Idade: entre 0 e 150;
# c.Salário: maior que zero;
# d.Sexo: 'f' ou 'm';
# e.Estado Civil: 's', 'c', 'v', 'd';

while True:

    nome = input('Nome: ')

    while len(nome) <= 3:
        print('Erro, digite novamente')
        nome = input('Nome: ')

    idade = int(input('Idade: '))

    while idade > 150:
        print('Erro, digite novamente')
        idade = int(input('Idade: '))

    salario = float(input('Salário: '))

    while salario <= 0:
        print('Erro, digite novamente')
        salario = float(input('Salário: '))

    sexo = str(input('Sexo F/M: ')).upper()

    while sexo not in ['F', 'M']:
        print('Erro, digite novamente')
        sexo = str(input('Sexo F/M: ')).upper()
    
    estado_civil  = str(input('Estado civil: S = Solteiro / C = Casado / V = Viuvo / D = Divorciado: ')).upper()

    while estado_civil not in ['S', 'C', 'V', 'D']:
        print('Erro, digite novamente')
        estado_civil  = str(input('Estado civil: S = Solteiro / C = Casado / V = Viuvo / D = Divorciado: ')).upper()
    
    break