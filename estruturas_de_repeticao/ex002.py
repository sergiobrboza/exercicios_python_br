# 2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    user = str(input('Digite o nome de usuario: '))
    senha = str(input('Digite a senha: '))
    if user == senha:
        print('Erro, senha fraca')
    elif user != senha:
        print('Usuario criado com sucesso!')
        break