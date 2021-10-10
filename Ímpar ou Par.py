#Faça um programa que jogue ÍMPAR OU PAR com o computador. O jogo só será interrompido quando o jogador PERDER,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('==== DESAFIO 68 ====\n')
print('JOGO JOGADO:\n\n')
from random import randint
from random import choice
cont = 0
while True:
    print('+-'*20)
    jogador = int(input('Jogue um Valor de 0 a 9: '))
    computador = randint(0, 9)
    soma = jogador + computador
    lista = ['I', 'P']
    PC = choice(lista)
    if soma % 2 == 0:
        eaí = 'PAR'
    else:
        eaí = 'ÍMPAR'
    escolha = str(input('ÍMPAR OU PAR? [I/P] ')).upper().strip()
    if escolha in 'I':
        eaí2 = 'ÍMPAR'
    elif escolha in 'P':
        eaí2 = 'PAR'
    print(f'Você escolheu {jogador} e eu escolhi {computador}, deu {soma}. {eaí}!')
    if eaí2 != eaí:
        break
    else:
        cont += 1
print('+-'*20)
print('Você perdeu!')
print(f'GAME OVER! VOCÊ VENCEU {cont} VEZES.')
