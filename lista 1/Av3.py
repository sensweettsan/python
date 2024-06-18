import math

# Lê um número do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo e calcula o valor apropriado
if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}.")
else:
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}.")
