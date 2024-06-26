# Lê um número do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 3 e por 7
if numero % 3 == 0 and numero % 7 == 0:
        print(f" {numero} É divisível por 3 e por 7")
else:
    print(f" {numero} NÃO é divisível por 3 e por 7")
