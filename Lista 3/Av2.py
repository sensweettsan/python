q = []
p = []
total = 0
vendas = int(input('Digite uma quantidade de vendas: '))

for n in range(vendas):
    quant = int(input('Digite uma quantidade de produtos: '))
    q.append(quant)
    preco = float(input('Digite um preço dos produtos: '))
    p.append(preco)
    total += quant * preco

    
print(f'Lista das quantidade: {q}')
print(f'Lista dos preços: {p}')

print(f"Faturamento mensal: {total}")