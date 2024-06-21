#definições das proprias funções#

def mensagem(a):
    print(f'Seja bem vindo(a {a}!!!)')

def dobro(x):
    return 2*x

nome = input('Digite seu nome: ')
mensagem(nome)

numero = int(input('Digite um numero: '))
print(f'O dobro de {numero} é {dobro(numero)}')

##############################################
import random

nomes = []
while True:
    nome= input('Digite um nome: ')
    if nome == "-1":
        break
    else:
        nomes.append(nome)

print(f'Número de pessoas: {len(nomes)}')
print(f'Lista de nomes: {nomes}')
nomesOrdenados = sorted(nomes)
print(f'Lista de nomes em ordem alfabética: {nomesOrdenados}')

print(f"O terceiro nome informado é {nomes[2]}")

random.seed()
sorteado = random.randint(0, len(nomes))
print(f"O nome sorteado foi{nomes[sorteado]}")