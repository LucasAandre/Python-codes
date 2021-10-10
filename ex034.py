# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print('==== DESAFIO 34 ====\n')
salario = float(input('Por favor digite o valor de seu salário: R$'))
if salario <= 1250:
    aumento = salario * 1.15
    print('Seu salário de R${} receberá um aumento de 15%'.format(salario))
    print('Seu novo salário com o aumento passará a custar: R${:.2f}'.format(aumento))
else:
    aumento = salario * 1.10
    print('Seu salário de R${} receberá um aumento de 10%'.format(salario))
    print('Seu novo salário com o aumento passará a custar: R${:.2f}'.format(aumento))
