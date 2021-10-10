'''
084. Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
		DICA: Identificar o maior/menor peso e mostrar a qual pessoa se refere.
'''

print('==== DESAFIO 84 ====\n')
print('OLHA A DIETA!\n\n')

inscritos = list()
dados = []
total = 0
pesado = leve = 0.00

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [KG]: ')))
    if len(inscritos) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    inscritos.append(dados[:])
    dados.clear()
    total += 1
    escolha = str(input('Deseja continuar? [S/N]: ')).upper()
    if escolha == 'N':
        break

print('-='*30)

#a
print(f'Ao todo, foram cadastradas {total} pessoas.')

#b
print(f'O maior peso declarado foi {pesado} Kg. Cuidado', end=' ')
for i in inscritos:
    if i[1] == pesado:
        print(f'{i[0]}', end= ' | ')
print('.')

#c
print(f'Já o menor peso, foi de {leve} Kg. Opa opa,', end=' ')
for i in inscritos:
    if i[1] == leve:
        print(f'{i[0]} | ', end='')
print('.')