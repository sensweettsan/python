# Função para calcular o peso ideal para homens
def peso_ideal_homem(altura):
    peso_ideal = 72.7 * altura - 58
    return peso_ideal

# Função para calcular o peso ideal para mulheres
def peso_ideal_mulher(altura):
    peso_ideal = 62.1 * altura - 44
    return peso_ideal

# Lê a altura do usuário
altura = float(input("Digite a altura (em metros): "))

# Lê o sexo da pessoa
sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

# Verifica o sexo e calcula o peso ideal utilizando a função correspondente
if sexo == "M":
    peso_ideal = peso_ideal_homem(altura)
    print(f"O peso ideal para um homem com altura {altura}m é {peso_ideal:.2f} kg.")
elif sexo == "F":
    peso_ideal = peso_ideal_mulher(altura)
    print(f"O peso ideal para uma mulher com altura {altura}m é {peso_ideal:.2f} kg.")
else:
    print("Sexo não reconhecido. Por favor, digite M para masculino ou F para feminino.")
