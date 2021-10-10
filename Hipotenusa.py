# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#  calcule e mostre o comprimento da hipotenusa.
from math import hypot
print('==== DESAFIO 17 ====\n')
print('Resolução do Teorema de Pitágoras:\n ')
CO = float(input('Por favor digite o valor do comprimento do Cateto Oposto do Triâmgulo Retângulo: '))
CA = float(input('Agora por favor digite o valor do comprimento do Cateto Adjacente: '))
Hip = hypot(CO, CA)
print('O valor do comprimento da Hipotenusa desse Triângulo Retângulo é: {:.2f}'.format(Hip))

# Eu poderia realizar usando a fórmula matemática




