# Refaça o DESAFIO 009, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um LAÇO FOR.

from time import sleep
print('==== DESAFIO 49 ====\n')
print('Olha a TABUADA:\n\n')
vi = int(input('Digite um Valor Inteiro: '))
mult = 0
print('-*' * 12)
for result in range(vi, vi * 11, vi):
    mult += 1
    print('{} x {:2} = {}'.format(vi, mult, result))
    sleep(1)
print('-*' * 12)
print('\nFIM')