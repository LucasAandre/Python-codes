#Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.

print('==== DESAFIO 52 ====\n')
print('Número Primo (ou não):\n\n')
núm = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes,'.format(núm, tot), end=' ')
if tot == 2:
    print('por isso ele É PRIMO!')
else:
    print('por isso ele NÃO É PRIMO!')
