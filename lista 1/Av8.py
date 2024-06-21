# Lê o ano de nascimento e o ano atual do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# Verifica se o ano de nascimento é válido
if ano_nascimento > 0 and ano_nascimento <= ano_atual:
    idade = ano_atual - ano_nascimento
    print(f"A idade da pessoa é {idade} anos.")
else:
    print("Ano de nascimento inválido.")
