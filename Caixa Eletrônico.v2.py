#Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO. No início, pergunte ao usuário qual será o VALOR A
#SER SACADO (número inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('==== DESAFIO 71 ====\n')
print('='*30)
print('{:^30}'.format('BANCO LADS'))
print('='*30)
#Quando chegar a zero (0), break neles!
print('Cédulas disponíveis:\nR$50\nR$20\nR$10\nR$1\n')
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO LADS!')
