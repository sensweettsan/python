
nome = input('Digite seu nome:')
sexo = input('Digite seu sexo:')
altura = float(input('Digite sua altura: '))

if sexo == "Masculino":
    print('Seu peso ideal é: ',round((72.7*altura)-58,2))
elif sexo == "Feminino":
    print('Seu peso ideal é: ', round((62.1*altura)-44.7,2))
    
    
#############################################################
#correção da atividade pelo wisner
#altura = float(input("Digite a altura: "))
#sexo = input('Digite o sexo ')

#pesoIdeal = 0.0 
#if(sexo.upper() == 'M'): # lower e basicamente colocar as letras em minusculo / upper colocar as letras em masculino 
  #  pesoIdeal = (72.7*altura)-58
#else:
  #  print("O sexo informado deve ser M para masculino ou F para femenino. ")

#if(pesoIdeal >0):
  #  print("O sexo informado foi: ", sexo.upper())
#    print("Seu peso idael é: ",round(pesoIdeal,2))

#############################################################################