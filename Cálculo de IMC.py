#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
#tabela abaixo:
#- Abaixo de 18.5: Abaixo do Peso
#- Entre 18.5 a 25: Peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

print('==== DESAFIO 43 ====\n\n')
print('Cálculo de IMC:\n')
nome = str(input('Olá! Por favor digite seu nome: '))
peso = float(input('Digite seu peso (em KG): '))
altura = float(input('Qual a sua altura? (em Metros): '))
IMC = (peso / altura**2)
print('{}, seu IMC é {:.2f} e:'.format(nome, IMC))
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= IMC <= 25:
    print('Você está com o peso ideal.')
elif 25 < IMC <= 30:
    print('Você está com sobrepeso.')
elif 30 < IMC <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')

