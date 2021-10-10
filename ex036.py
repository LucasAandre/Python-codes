#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA
# CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('==== DESAFIO 36 ====\n\n')
print('Empréstimo:\n')
nome = input('Por favor digite seu nome: ')
ValorDaCasa = float(input('Digite o Valor do Empréstimo (Valor da Casa): R$'))
salario = float(input('Qual o Valor de seu Salário?: R$'))
anos = int(input('Em quantos ANOS você pretende pagar esse empréstimo?: '))
meses = (anos * 12)
prestacao = (ValorDaCasa / meses)
condicao = ( 0.3 * salario)
if prestacao > condicao:
    print('\nEMPRÉSTIMO NÃO APROVADO.')
else:
    print('\nEMPRÉSTIMO APROVADO.')

'''
casa = float(input('Valor da Casa: R$'))
salário = loat(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${.:2f}'.format(prestação))
if prestação <= mínimo;
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!)
'''