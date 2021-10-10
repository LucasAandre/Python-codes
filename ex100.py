'''
100. Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar qual a soma
entre todos os valores PARES sorteados pela função anterior.
'''

from random import randint
from time import sleep

def sorteio(lista):
    print('SORTEIO:')
    for c in range(0, 5):
        num = randint(0, 100)
        lista.append(num)
        print(num, end=' ', flush=True)
        sleep(0.6)
    print(f'\nOs números sorteados foram: {números}')


def somaPar(lista):
    print('\nSOMA DOS VALORES PARES:')
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A somatória dos valores pares é: {soma}')


números = list()
sorteio(números)
somaPar(números)

