'''
075. Desenvolva um programa que leia QUATRO VALORES pelo TECLADO e guarde-os em uma TUPLA. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números PARES.
'''

print('==== DESAFIO 75 ====\n\n')
escolha = 'S'
while escolha in 'Ss':
    a = int(input('Digite o 1º valor inteiro: '))
    b = int(input('Digite o 2º valor inteiro: '))
    c = int(input('Digite o 3º valor inteiro: '))
    d = int(input('Digite o 4º valor inteiro: '))

    abcd = (a, b, c, d)
    print('='*40)
    print(abcd)

    #a
    if abcd.count(9) >= 1:
        print('=' * 40)
        print('Você digitou {} número(s) 9'.format(abcd.count(9)))
    else:
        print('=' * 40)
        print('Você não digitou nenhum número 9')

    #b
    if abcd.count(3) >= 1:
        print('=' * 40)
        print(f'O primeiro número 3 aparece na {abcd.index(3)+1}ª posição')
    else:
        print('=' * 40)
        print('Não foi digitado nenhum valor 3')

    #c
    cont_par = 0
    print('=' * 40)
    print('Os valores pares são:', end=' ')
    for par in abcd:
        if par % 2 == 0:
            cont_par += 1
            print(f'{par}', end=' | ')
        #else:
        #    print(f'\n{par}', end=' | ')
    if cont_par == 0:
        print('Nenhum valor par foi digitado.')
        print('=' * 40)
    escolha = str(input('\nDeseja continuar?[SIM/NÃO]: ')).strip()[0]

