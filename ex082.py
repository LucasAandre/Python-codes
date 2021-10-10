'''
082. Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma lista. Depois disso, crie DUAS LISTAS EXTRAS que vão
conter apenas os valores PARES e os valores ÍMPARES digitados, respectivamente. Ao final, mostre o conteúdo das TRÊS
LISTAS geradas.
'''

print('==== DESAFIO 82 ====\n')
print('Listas, Pares e Ímpares\n\n')

#Minha resolução:

lista = list()
pares = []
ímpares = list()

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        ímpares.append(num)
    escolha = str(input('Deseja continuar?[S/N]: ')).upper()
    if escolha == 'N':
        break
print('='*30)
print(f'Sua lista é: {lista}')
print('Os valores pares são: {}'.format(pares))
print(f'Os valores ímpares{ímpares}')




#Resolução do Guanabara:
'''
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break
for i, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        ímpares.append(valor)
print('='*30)
print(lista)
print(pares)
print(ímpares)
'''
