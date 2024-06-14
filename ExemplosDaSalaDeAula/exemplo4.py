''''''
#while
''''''

contador = 0
contM = 0 
contF = 0 
mediaF = 0.0
mediaM = 0.0 
maior = 0 
menor = 99

qtde = input('Digite a quantidade de alunos: ')


while contador < qtde:
    sexo = input('Digite seu sexo: ')
    altura = float(input('Digite a altura: '))

    if altura > maior:
        maior = altura

    if menor > altura:
        menor = altura

    if sexo.upper() == 'F':
        contF = contF + 1
        mediaF = mediaF + altura
    elif sexo.upper() == 'M':
        contM = contM + 1
        mediaM = mediaM + altura
    else:
        print('Sexo informado e inválido.')
        continue
    contador = contador + 1


print('A quantidade de alunos do sexo feminino é: ', contF)
print('A quantidade de alunos de sexo masculino é: ', contM)


if contF > 0:
    mediaF = mediaF / contF

if contM > 0:
    mediaM = mediaM / contM


print(round('A media de alturas do sexo feminino é: ', mediaF))
print(round('A media de alturas do sexo Masculina é: ', mediaM))

print('A maior altura é: ', maior)
print('A maior altura é: ', menor)