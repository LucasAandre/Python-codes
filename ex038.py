#Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print('==== DESAFIO 38 ====\n\n')
print('Comparação de Valores:\n')
num1 = int(input('Digite o 1º Número Inteiro: '))
num2 = int(input('Digite o 2º Número Inteiro: '))
if num1 > num2:
    print('O número {} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que {}'.format(num2, num1))
else:
    print('Esses valores são iguais.')
