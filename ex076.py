'''
076. Crie um programa que tenha uma TUPLA única com NOMES DE PRODUTOS e seus respectivos PREÇOS, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma TABULAR.
                             listagem = ('Pão', 1, 'Leite', 3.50)
'''
print('==== DESAFIO 76 ====\n')
print('Tabela de Preços:\n\n')

print('Bem-vindo à Lanchonete OS NOVINHOS ESTÃO DE PARABÉNS:\n\nConfira nossa tabela de preços:\n')
print('='*50)
tabela = ('X-Burger', 4.50, 'X-Salada', 3.90, 'X-Picanha', 6.00, 'X-Tudo', 8.00, 'Água Mineral s/ gás', 2.00,
          'Água Mineral c/ gás', 2.50)
#a = 0
#b = 1

for c in range(0, len(tabela), 2):
    print(f'{tabela[c]:.<30}..........R${tabela[c+1]}')
    #a += 2
    #b += 2
print('='*50)
print('\n')

