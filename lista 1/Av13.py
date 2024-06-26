# Lê a idade do usuário
idade = int(input("Digite a idade : "))

# Verifica a classe eleitoral com base na idade
if idade < 16:
    print("Classe Eleitoral: NÃO ELEITOR - abaixo de 16 anos")
elif idade >= 18 and idade >= 65:
    print("Classe Eleitoral: ELEITOR OBRIGATÓRIO - entre 18 e 65 anos")
else:
    print(f"Idade:{idade} - Eleitor facultativo")


