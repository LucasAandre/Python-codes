#Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário.
#O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.
print('==== DESAFIO 67 ====\n')
print('TABUADA HELP:\n\n')
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 10)
    if num < 0:
        break
    else:
        UM = num * 1
        DOIS = num * 2
        TRES = num * 3
        QUATRO = num * 4
        CINCO = num * 5
        SEIS = num * 6
        SETE = num * 7
        OITO = num * 8
        NOVE = num * 9
        DEZ = num * 10
        print(f'{num} x {1} = {UM}')
        print(f'{num} x {2} = {DOIS}')
        print(f'{num} x {3} = {TRES}')
        print(f'{num} x {4} = {QUATRO}')
        print(f'{num} x {5} = {CINCO}')
        print(f'{num} x {6} = {SEIS}')
        print(f'{num} x {7} = {SETE}')
        print(f'{num} x {8} = {OITO}')
        print(f'{num} x {9} = {NOVE}')
        print(f'{num} x {10} = {DEZ}')
        print('-'*10)
print('PROGRAMA TABUADA HELP ENCERRADO!')
