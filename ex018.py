# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
print('==== DESAFIO 18 ====\n')
print('Seno, Cosseno e Tangente:\n')
ang = float(input('Por favor digite a medida do ângulo em questão: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O Seno de {}º vale: {:.2f}'.format(ang, sen))
print('O Cosseno de {}º vale: {:.2f}'.format(ang, cos))
print('A Tangente de {}º tem medida de: {:.2f}'.format(ang, tang))

