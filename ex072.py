'''
072. Crie um programa que tenha um TUPLA totalmente preenchida com uma contagem por extensão, de ZERO até VINTE.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por EXTENSO(16 = dezesseis). - Sem if else
                                             FOR: índice = c = num
'''

dados = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE',
         'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if (num >= 0 and num <= 20):
        print(f'Você digitou o número {dados[num]}')
        escolha = str(input('Deseja continuar?[SIM / NÃO] ')).upper()
        if (escolha == 'NÃO'):
            break
    else:
        print('ERRO!', end='')
print('\nFIM!')

