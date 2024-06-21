# Lê a sigla do estado do usuário
sigla_estado = input("Digite a sigla do seu estado (por exemplo, RJ, SP, MG): ").upper()

# Verifica a sigla do estado e imprime a mensagem correspondente
if sigla_estado == "RJ":
    print("Carioca")
elif sigla_estado == "SP":
    print("Paulista")
elif sigla_estado == "MG":
    print("Mineiro")
else:
    print("Outro estado")
