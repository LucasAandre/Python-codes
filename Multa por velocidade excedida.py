# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

print('==== DESAFIO 29 ====\n\n')
velocidade = float(input('Por gentileza digite a velocidade de seu carro em Km/h: '))
if velocidade > 80:
    print('Você excedeu o limite de 80 Km/h! Está mutado!')
    multa = (velocidade - 80) * 7
    print('Sua multa tem o valor de: R${:.2f}'.format(multa))
else:
    print('Muito Bem! Você não ultrapassou o limite de 80 Km/h. Continue assim!')
