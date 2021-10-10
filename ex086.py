'''
086. Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a
matriz na tela, com a formatação correta.
				                            DICA:
				            Digite um valor para a posição [0,0]:
				            Digite um valor para a posição [0,1]:
                            Digite um valor para a posição [0,2]:
                            Digite um valor para a posição [1,0]:
                                            ...
                            Digite um valor para a posição [2,0]:
                                            ...
'''

print('==== DESAFIO 86 ====\n')
print('Matriz com Lista:\n\n')

linha0 = list()
linha1 = list()
linha2 = list()

coluna0 = []
coluna1 = []
coluna2 = []

for lzero in range(0, 3):
    linha0.append(int(input(f'Digite um valor para a posição [0, {lzero}]: ')))

for lum in range(0, 3):
    linha1.append(int(input(f'Digite um valor para a posição [1, {lum}]: ')))

for ldois in range(0, 3):
    linha2.append(int(input(f'Digite um valor para a posição [2, {ldois}]: ')))

coluna0.append(linha0[0])
coluna0.append(linha1[0])
coluna0.append(linha2[0])

coluna1.append(linha0[1])
coluna1.append(linha1[1])
coluna1.append(linha2[1])

coluna2.append(linha0[2])
coluna2.append(linha1[2])
coluna2.append(linha2[2])

print('=-'*30)
print('Sua matriz fica:\n')
#for c in range(0, 3):
print(f'{linha0[0]} | {linha0[1]} | {linha0[2]}')
print(f'{linha1[0]} | {linha1[1]} | {linha1[2]}')
print(f'{linha2[0]} | {linha2[1]} | {linha2[2]}')

#Resolução do Guanabara:
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
print('=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
'''
