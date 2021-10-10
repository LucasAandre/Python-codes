#Crie um programa de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
print('==== DESAFIO 54', ('='*4))
print('Grupo da Maioridade:\n\n')
from datetime import date
atual = date.today().year
#núm = 0
velho = 0
novo = 0
for pessoa in range(1, 8):
    #núm += 1
    nasc = int(input('Em que ano a {}º pessoa nasceu?: '.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        velho += 1
    else:
        novo += 1
print('Das {} pessoas avaliadas, {} são MAIORES DE IDADE e {} são MENORES DE IDADE'.format(pessoa, velho, novo))

