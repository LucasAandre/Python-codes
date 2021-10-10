#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 TERMOS.

print('==== DESAFIO 62 ====\n')
print('Progressão Aritmética:\n\n')
escolha = int(input('''Digite o número de sua escolha:
[1] Cálculo com o 1º TERMO e a RAZÃO
[2] Cálculo com o 1º e o 2º TERMO
'''))
if escolha == 1:
    n1 = int(input('Digite o 1º Termo dessa P.A: ' ))
    r = int(input('Digite a Razão dessa P.A: '))
elif escolha == 2:
    n1 = int(input('Digite o 1º Termo dessa P.A: '))
    n2 = int(input('Digite o 2º Termo dessa P.A: '))
    r = n2 - n1
else:
    print('Opção Inexistente! Por favor execute novamente o programa.')
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Progressão Finalizada com {} termos mostrados'.format(total))
