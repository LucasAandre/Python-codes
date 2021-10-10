#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai
#tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from time import sleep
from random import randint
print('==== DESAFIO 58 ====\n')
print('Jogo da Advinhação:\n\n')
print('-='*20)
print('Pensei em um número inteiro entre 0 e 10. Que número é esse?')
print('-='*20)
jogador = int(input('Digite o número escolhido: '))
print('\nPROCESSANDO...')
PC = randint(0, 10)
sleep(3)
tentativa = 0
while jogador != PC:
    jogador = int(input('ERROOOOOOU! Mais uma chance, tente advinhar o número que pensei: '))
    tentativa += 1
print('MUITO BEM! Foi no {} mesmo que pensei.'.format(PC))
print('Você precisou de {} chances para acertar'.format(tentativa))
print('GAME OVER!')
