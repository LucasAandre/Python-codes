'''
092. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
				DICA: 35 anos de contribuição para a aposentadoria
'''
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = (datetime.now().year - nasc)
resp = str(input('Possui Carteira de Trabalho?: ')).upper()
if resp in 'SIM':
    dados['CTPS'] = int(input('Número da Carteira de Trabalho: '))
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year))
else:
    dados['CTPS'] = 0
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor de {v}')

