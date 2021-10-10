# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
print(('='*4), 'DESAFIO 16', ('='*4))
import math
print('Porção Inteira de Valores:\n ')
numR = float(input('Por favor digite um Número Real: '))
ParteInteira = math.trunc(numR)
print('A Porção Inteira de {0} é igual a: {1}'.format(numR, ParteInteira))

'''VR = float(input('Por favor digite um Número Real: '))
print('A Porção Inteira de {} é: {}'.format(VR, int(VR)))'''


