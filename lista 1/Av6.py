# Lê um número do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 3 e por 7
if numero % 3 == 0 and numero % 7 == 0:
    print("É divisível por 3 e por 7")
else:
    print("NÃO é divisível por 3 e por 7")
