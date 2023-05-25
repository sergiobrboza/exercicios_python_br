# 15.A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
def fibonacci(n):
    termo1 = 1
    termo2 = 1
    
    if n <= 0:
        print("O valor de n deve ser maior que 0.")
        return
    
    print(termo1)
    print(termo2)
    
    for i in range(3, n+1):
        proximo_termo = termo1 + termo2
        print(proximo_termo)
        
        termo1 = termo2
        termo2 = proximo_termo

n = int(input("Digite o valor de n: "))

fibonacci(n)