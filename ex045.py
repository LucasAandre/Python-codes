#Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import choice
from time import sleep
print('==== DESAFIO 45 ====\n\n')
print('JOKENPÔ!:\n')
print('\033[1;30mPEDRA\033[m\n\033[1;37mPAPEL\033[m\n\033[1;34mTESOURA\033[m')
usuario = str(input('Digite sua escolha: ')).upper()
e1 = 'PEDRA'
e2 = 'PAPEL'
e3 = 'TESOURA'
lista = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = choice(lista)
print('Aguarde a minha vez...')
sleep (3)
print('Eu escolho: {}\n\n'.format(maquina))
sleep (2)
if usuario == 'PEDRA':
    if maquina == 'PEDRA':
        print('Shiiiii... EMPATOU!')
    elif maquina == 'PAPEL':
        print('HIHI, EU GANHEI!!!')
    elif maquina == 'TESOURA':
        print('VOCÊ VENCEU ESSA! NA PRÓXIMA EU VOU JOGAR PRA VALER HAHA')
elif usuario == 'PAPEL':
    if maquina == 'PEDRA':
        print('AH NÃO! VOCÊ VENCEU ESSA...')
    elif maquina == 'PAPEL':
        print('NEM EU E NEM VOCÊ, DEU EMPATE!')
    elif maquina == 'TESOURA':
        print('GAAAAAANHEI! BOA SORTE NA PRÓXIMA VEZ.')
elif usuario == 'TESOURA':
    if maquina == 'PEDRA':
        print('EU SOU INCRÍVEL! GANHEI ESSA ;)')
    elif maquina == 'PAPEL':
        print('VOCÊ MOSTROU QUE É BOM NISSO. VOCÊ VENCEU!')
    elif maquina == 'TESOURA':
        print('QUERO IR DE NOVO... EMPATE NÃO TEM GRAÇA...')
else:
    print('OPS, SÓ VALE PEDRA, PAPEL E TESOURA ;)')