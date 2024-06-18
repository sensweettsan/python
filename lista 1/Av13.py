# Lê a idade do usuário
idade = int(input("Digite a idade da pessoa: "))

# Verifica a classe eleitoral com base na idade
if idade < 16:
    print("Classe Eleitoral: NÃO ELEITOR - abaixo de 16 anos")
elif 18 <= idade <= 65:
    print("Classe Eleitoral: ELEITOR OBRIGATÓRIO - entre 18 e 65 anos")
elif 16 <= idade < 18 or idade > 65:
    print("Classe Eleitoral: ELEITOR FACULTATIVO - 16 a 18 anos e mais de 65 anos")
else:
    print("Idade inválida.")  # Caso a idade seja negativa ou zero


