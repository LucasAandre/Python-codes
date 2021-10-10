#Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da progressão
#usando a estrutura WHILE.

print('==== DESAFIO 61 ====\n')
print('P.A.:\n\n')
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
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += r
    cont += 1
print('FIM')
