# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


print('==== DESAFIO 30 ====\n')
print('Valor Ímpar ou Par:\n\n')
ni = int(input('Por favor digite um Número Inteiro: '))
resultado = ni % 2# Se o resultao for 1, significa que o número é ímpar. Se for 0, par.
# O resto de qualquer divisão de qualquer número ÍMPAR por 2 é igual a 1
# O resto de qualquer divisão de qualquer número PAR por 2 é igual a 0
if resultado == 1:
    print('O número {} é um número ÍMPAR.'.format(ni))
else:
    print('O número {} é um número PAR.'.format(ni))
print('\n\nATÉ MAIS...')
