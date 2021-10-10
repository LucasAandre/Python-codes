'''
098. Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
a contagem. Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada (o usuário vai personalizar)
'''

from time import sleep
def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'\nContagem de {início} até {fim}, de {passo} em {passo}:')
    sleep(1)

    if início < fim:
        result = início
        while result <= fim:
            print(f'{result}', end=' ', flush=True)
            sleep(0.5)
            result += passo
        print(' SE FINITO!')
    else:
        result = início
        while result >= fim:
            print(f'{result}', end=' ', flush=True)
            sleep(0.5)
            result -= passo
        print(' SE FINITO!')


#A)
contador(1, 10, 1)

#B)
contador(10, 0, 2)

#C)
print('\nPersonalize a contagem! Defina:')
início = int(input('Início da contagem: '))
fim = int(input('Final da contagem: '))
passo = int(input('Passo da contagem: '))
contador(início, fim, passo)