'''
073. Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da Tabela do Campeaonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a) Apenas os 5 PRIMEIROS colocados.
b) Os ÚLTIMOS 4 colocados da tabela.
c) Uma lista com os times em ORDEM ALFABÉTICA.
d) Em que POSIÇÃO na tabela está o time da CHAPECOENSE.
'''
print('==== DESAFIO 73 ====\n\n')
print('Brasileirão 2018 - Rodada 7:\n')

brasileiro = ('Flamengo', 'Fluminense', 'Atlético-MG', 'São Paulo', 'Grêmio', 'Corinthians', 'Palmeiras',
               'Internacional', 'Sport', 'Cruzeiro', 'América-MG', 'Botafogo', 'Vasco', 'Vitória', 'Bahia', 'Santos',
               'Atlético-PR', 'Chapecoense', 'Ceará', 'Paraná')

print('='*30)
print(f'1º {brasileiro[0]}\n2º {brasileiro[1]}\n3º {brasileiro[2]}\n4º {brasileiro[3]}\n5º {brasileiro[4]}\n'
      f'6º {brasileiro[5]}\n7º {brasileiro[6]}\n8º {brasileiro[7]}\n9º {brasileiro[8]}\n10º {brasileiro[9]}\n'
      f'11º {brasileiro[10]}\n12º {brasileiro[11]}\n13º {brasileiro[12]}\n14º {brasileiro[13]}\n15º {brasileiro[14]}\n'
      f'16º {brasileiro[15]}\n17º {brasileiro[16]}\n18º {brasileiro[17]}\n19º {brasileiro[18]}\n20º {brasileiro[19]}')
print('='*30)

#a
print('\n\nOs 5 primeiros colocados são:')
print(brasileiro[:5])

#b
print('\n\nOs 4 últimos colocados são:')
print(brasileiro[-4:])

#c
print('\n\nA classificação em ordem alfabética fica:')
print(sorted(brasileiro))

#d
print(f'\n\nA {brasileiro[17]} é o {brasileiro.index("Chapecoense")+1}º colocado')

'''
disponibilizo meu código:
campeonato = ('Flamengo','Fluminense','Atlético','São Paulo','Grêmio',
            'Corinthians','Palmeiras','Internacional','Sport Recife',
            'Cruzeiro','América-MG','Botafogo','Vasco da Gama','Vitória',
            'Bahia','Santos','Atlético-PR','Chapecoense','Ceará','Paraná')

print(f'a) Os cinco primeiros colocados são: ')
for cont in range(0,5):
    print(f'{campeonato[cont]}')

print(f'b) Os últimos 4 colocados são: ')
for cont in range(16,len(campeonato)):
    print(f'{campeonato[cont]}')

print(f'c) Os times em ordem alfabética são:')
for x in sorted(campeonato):
    print(f'{x}')

print(f"d) O time da Chapecoense está na {campeonato.index('Chapecoense')+1}a posição.")﻿
'''

