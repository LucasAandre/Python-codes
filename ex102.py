'''
102. Crie um programa que tenha uma função fatorial () que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.
Adicione também as docstrings da função.
'''

def fatorial(n, show = False):
    """
    -> Cálculo de um fatorial
    :param n: O valor a ser calculado
    :param show: (opcional) mostrar o passo a passo ou não
    :return: O valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


#Programa Principal
n = int(input('Deseja saber o fatorial de qual valor inteiro? '))
opção = int(input('Deseja visualizar o passo a passo do cálculo de fatorial? [1 para sim e 2 para não]? '))
if opção == 1:
    show = True
else:
    show = False
print(fatorial(n, show))
#help(fatorial)