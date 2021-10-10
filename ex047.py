# Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo entre 1 e 50.
print('=== DESAFIO 47 ====\n')
print('Números Pares de 1 a 50:\n\n')
nome = str(input('Qual o seu nome?\n'))
print('\nOlá {}! Esses são TODOS OS NÚMEROS PARES que estão no intervalo entre 01 e 50:'.format(nome))
for pares in range(2, 51, 2):
    print(pares, end=' ')
print('\nFIM')
