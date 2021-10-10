'''
091. Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogador1 = str(input('Nome do jogador 1: '))
jogador2 = str(input('Nome do jogador 2: '))
jogador3 = str(input('Nome do jogador 3: '))
jogador4 = str(input('Nome do jogador 4: '))

jogo = {jogador1: randint(1, 6),
        jogador2: randint(1, 6),
        jogador3: randint(1, 6),
        jogador4: randint(1, 6)}

ranking = list()
print('\nValores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]:<2} com {v[1]}')
    sleep(1)