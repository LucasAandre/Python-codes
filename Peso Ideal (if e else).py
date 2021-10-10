sexo = (input('Por favor digite seu sexo (M/F): '))
altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Seu peso (em Kg): '))

if (sexo == 'M'):
    PesoIdeal = (72.7 * altura) - 58
else:
    PesoIdeal = (62.1 * altura) - 44.7

if (peso > PesoIdeal):
    print('Você está acima do seu peso ideal: {}'.format(PesoIdeal))
elif (peso < PesoIdeal):
    print('Você está abaixo do seu peso ideal: ', PesoIdeal)
else:
    print('Você está no seu peso ideal: {}'.format(PesoIdeal))
