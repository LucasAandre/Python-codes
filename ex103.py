'''
103. Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.
'''


def ficha(jog='<desconhecido>', gol=0):
    print(f'O {jog} marcou {gol} gol(s) no campeonato.')


#Programa principal
nome = str(input('Digite o nome do jogador analisado: '))
gols = str(input('Digite a quantidade de gols desse jogador no campeonato: '))
if gols == '':
    gols = 0
else:
    gols = int(gols)
if nome.strip() == '': #Se a resposta, sem os espaços, estiver vazia
    ficha(gol=gols) #Define apenas o segundo parâmetro como preenchido
else:
    ficha(nome, gols)
