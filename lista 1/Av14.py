import math

# Lê os coeficientes a, b e c
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Verifica se é uma equação de segundo grau (a != 0)
if a == 0:
    print("Não é equação do segundo grau.")
else:
    # Calcula o discriminante
    delta = b**2 - 4 * a * c
    
    # Verifica o valor do discriminante
    if delta < 0:
        print("Não há raízes reais para esta equação.")
    else:
        # Calcula as raízes
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        
        # Imprime as raízes
        print(f"As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}")
