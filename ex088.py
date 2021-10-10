'''
088. Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
print('==== DESAFIO 88 ====\n')

jogos = list()
jogo = []

print(('='*10), 'MEGA-SENA LADS', ('='*10))
print('\n')

#limite = (0, limite)

limite = int(input('Olá! Seja bem-vindo\nQuantos jogos deseja fazer?: '))

for c in range(0, limite):
    for cont in range(0, 6):
        num = randint(1, 60)
        jogo.append(num)
        jogos.append(jogo)
    print(f'Jogo {c+1}: {jogos[c]}')
    jogo.sort()
print()
print('Jogos finalizados.\nBoa sorte!')


#Resolução escolhida dos Comentários:
#Função Sample
'''
from random import sample
from time import sleep

jogos = list()
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
palpites = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {palpites} JOGOS  -=-=-=')
for p in range(palpites):
    jogos.append(sample(range(1, 60), 6))
for n, j in enumerate(jogos):
    print(f'Jogo {n+1}: {sorted(j)}')
    sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
'''