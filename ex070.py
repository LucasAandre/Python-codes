#Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa deverá perguntar se o USUÁRIO vai continuar.
#No final, mostre:
#(a)Qual é o TOTAL GASTO na compra.
#(b)Quantos produtos custam MAIS de R$1000.
#(c)Qual é o NOME do produto mais BARATO.
print('==== DESAFIO 70 ====\n')
print('LOJAS LADS:\n\n')
total = mais = barato = cont = 0
ProdutoBarato = ''
while True:
    print('-'*35)
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor deste mesmo produto: R$'))
    total += valor
    cont += 1
    if valor > 1000:
        mais += 1
    if cont == 1 or valor < barato:
        barato = valor
        ProdutoBarato = produto
    escolha = str(input('Deseja continar a comprar? [S/N]: ')).upper()
    if escolha in 'N':
        break
print('-'*35)
print(f'\nO TOTAL GASTO na compra foi de R${total:.2f}')
print(f'Na sua compra, {mais} produtos custam mais de R$1000,00')
print(f'O {ProdutoBarato} é o produto mais barato da compra.')
