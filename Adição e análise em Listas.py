'''
079. Crie um programa onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-os em uma LISTA. Caso o número já
exista lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE.
'''

print('==== DESAFIO 79 ====\n\n')

valores = list()
while True:
    n = (int(input('Digite um valor para ser adicionado na lista: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor já digitado! Não vou adicionar.')
    escolha = str(input('Deseja continuar? [S/N]: ')).upper()
    if escolha in 'N':
        break
print('='*30)
valores.sort()
print(f'A lista ficou da seguinte forma: {valores}')
