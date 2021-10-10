'''Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
[1] Somar
[2] Múltiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

print('==== DESAFIO 59 ====\n')
print('Mini Calculadora (MESMO):\n\n')
n1 = float(input('Digite o 1º Número: '))
n2 = float(input('Digite o 2º Número: '))
print('Escolha uma das opções do Menu abaixao:')
escolha = int(input('''[1] Somar
[2] Múltiplicar
[3] Maior e Menor
[4] Novos Números
[5] Sair do Programa
'''))
while escolha != 5:
    if escolha == 1:
        print('SOMA: {} + {}'.format(n1, n2))
        soma = n1 + n2
        print('{} + {} = {:.2f}'.format(n1, n2, soma))
        escolha = int(input('Escolha outra opção: '))
    elif escolha == 2:
        print('MÚLTIPLICAR: {} x {}'.format(n1, n2))
        mult = n1 * n2
        print('{} x {} = {:.2f}'.format(n1, n2, mult))
        escolha = int(input('Escolha outra opção: '))
    elif escolha == 3:
        print('MAIOR E MENOR:')
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Esses números são iguais!')
        escolha = int(input('Escolha outra opção: '))
    elif escolha == 4:
        print('NOVOS NÚMEROS:')
        n1 = float(input('Digite o 1º Número: '))
        n2 = float(input('Digite o 2º Número: '))
        escolha = int(input('Escolha outra opção: '))
    else:
        print('Opção Inválida!')
        escolha = int(input('Escolha outra opção: '))
print('THE END')
