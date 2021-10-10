'''
094. Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um lista.
No final, mostre:
a) Quantas pessoas foram cadastradas.
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da média.
'''
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
#A)
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')
#B)
média = (soma / len(galera))
print(f'A média de idade é de: {média}')
#C)
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
#D)
print('As pessoas com idade acima da média são: ', end='')
for p in galera:
    if p['idade'] > média:
        print(f'{p["nome"]}', end=' ')
print()

