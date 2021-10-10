'''
090. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
o conteúdo da estrutura na tela.
'''

from time import sleep

dados = {'nome': '', 'média': '', 'situação': ''}

print('Preencha os dados:\n')
dados['nome'] = str(input('Nome do aluno: '))
dados['média'] = float(input('Média do aluno: '))

if dados['média'] >= 5.0:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'

print('\n>>> ARQUIVANDO... <<<')
sleep(1)
print()
print(f'Aluno: {dados["nome"]}')
print(f'Média: {dados["média"]}')
print(f'Situação: {dados["situação"]}')

