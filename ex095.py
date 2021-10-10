'''
095. Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
					Montar um painel com os dados finais de todos os jogadores impregando códigos a cada um e depois:
									DICA: "Mostrar dados de qual jogador?"
										Código 999 encerra o programa
'''


time = list()
jogador = dict()
partidas = list()
print('==== CONTROLE DE APROVEITAMENTO ====\n')
while True:
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Total de partidas de {jogador["Nome"]}: '))
    partidas.clear()
    for c in range (0, tot):
        partidas.append(int(input(f'  Quantidade de gols na partida {c+1}: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Por favor, responda S ou N')
    if resp == 'N':
        break
print('-='*30)
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k+1:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Deseja buscar os dados de qual jogador? [999 para parar] '))
    busca -= 1
    if busca == 998:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca+1}!')
    elif busca == -1:
        print(f'Erro! Não existe jogador com código {busca+1}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i+1}, o jogador fez {g} gols.')
    print('-' * 40)