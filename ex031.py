# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
#  por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print('==== DESAFIO 31 ====\n')
print('Preço de Viagem:\n\n')
distância = float(input('Por gentileza digite a DISTÂNCIA de sua viagem em Km: '))
if distância > 200:
    Passagem = (distância * 0.45)
    print('Sua Passagem custará: R${:.2f}'.format(Passagem))
else:
    Passagem = (distância * 0.5)
    print('Sua Passagem custará: R${:.2f}'.format(Passagem))
