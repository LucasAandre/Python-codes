'''
074. Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.
Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla.
                                If Else com os ÍNDICES
'''

from random import randint as luc

print('==== DESAFIO 74 ====\n')
print('Tupla Randômica:\n\n')

print('='*35)
while True:
    valor0 = luc(0, 9)
    valor1 = luc(0, 9)
    valor2 = luc(0, 9)
    valor3 = luc(0, 9)
    valor4 = luc(0, 9)

    valores = (valor0, valor1, valor2, valor3, valor4)

    if valor0 > valor1:
        maior = valor0
        menor = valor1
    else:
        maior = valor1
        menor = valor0
    if valor2 > maior:
        maior = valor2
    else:
        maior = maior
    if valor2 < menor:
        menor = valor2
    else:
        menor = menor
    if valor3 > maior:
        maior = valor3
    else:
        maior = maior
    if valor3 < menor:
        menor = valor3
    else:
        menor = menor
    if valor4 > maior:
        maior = valor4
    else:
        maior = maior
    if valor4 < menor:
        menor = valor4
    else:
        menor = menor

    print(valores)
    print(f'{maior} é o MAIOR número gerado e {menor} é o MENOR')

    escolha = str(input('Deseja continuar? [SIM/NÃO]: ')).lower()
    print('='*35)
    if escolha == 'não':
        break

print('\nSE FINITO!')
print(max(valores))
print(min(valores))
t(f'O número maior é {n_maior} O número menor é {n_menor}')
