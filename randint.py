# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('==== DESAFIO 28 ====\n\n')
print('-=-'*20)
print('Pensei em um número inteiro de 0 a 5! Que número é esse?')
print('-=-'*20)
jogador = int(input('\n\nPor favor digite o número escolhido: '))
print('\nPROCESSANDO...')
PC = randint(0, 5)
sleep(3)
if jogador == PC:
    print('MUITO BEM! Você acertou e me venceu!\n\n')
else:
    print('Que pena... Eu pensei no número {} e não no {}. VOCÊ PERDEU!\n\n'.format(PC, jogador))
print('GAME OVER')
