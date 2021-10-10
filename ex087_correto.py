'''
087. Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
print('=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print('=-'*30)
print(f'A soma dos valores pares é: {spar}')
print(matriz)
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da 3ª coluna vale: {scol}')
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > mai:
        mai = matriz[1][coluna]
print(f'O maior valor da 2ª linha é: {mai}')