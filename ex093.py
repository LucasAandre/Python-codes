'''
093. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos durante o campeonato.
{'nome': 'Joelson', 'gols': [2, 1, 0, 0, 3], 'total': 6}
'''
jogador = dict()
partidas = list()
print('==== CONTROLE DE APROVEITAMENTO ====\n')
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Total de partidas de {jogador["nome"]}: '))
for c in range (0, tot):
    partidas.append(int(input(f'  Quantidade de gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de valor {v}')
print('-='*30)
print(f'O {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, c in enumerate(partidas):
    print(f'  => Marcou {c} gols na partida {i+1}')
print(f'Foi um total de {jogador["total"]} gols.')
