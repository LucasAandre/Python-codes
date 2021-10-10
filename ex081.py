'''
Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma lista. Depois disso, mostre:
a) QUANTOS números foram digitados.
b) A lista de valores, ordenada de forma DECRESCENTE.
c) Se o valor 5 foi digitado e está ou não na lista.
'''

print('==== DESAFIO 81 ====\n')

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    escolha = str(input('Deseja continuar?[S/N]: ')).upper()
    if escolha in 'N':
        break
print('='*30)

print(f'A lista que você digitou ficou: {lista}')

#c
pos = lista.index(5)+1

#a
print(f'Essa lista possui {len(lista)} elementos')

#b
lista.sort(reverse=True)
print(f'Forma decrescente: {lista}')

#c
if 5 not in lista:
    print('Essa lista não possui nenhum valor 5')
else:
    print(f'Essa lista possui {lista.count(5)} valores 5, sendo que o primeiro aparece na {pos}ª posição.')
print('='*30)




