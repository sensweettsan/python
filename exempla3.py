#Estrutura condicional if

nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2

print('Sua média foi -->', media)

media = int (input('Digite sua média: ')) 
if media >= 6:
    print('Aprovado')
elif media < 5:
    print('Reprovado')
else:
    print('Reprovado')


