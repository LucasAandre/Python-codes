'''
078. Faça um programa que leia 5 VALORES NUMÉRICOS e guarde-os em uma LISTA. No final, mostre qual foi o MAIOR e o MENOR
 valor digitado e as suas respectivas POSIÇÕES na lista.
'''
print('==== DESAFIO 78 ====\n')
print('Maior e Menor em Lista:\n\n')

numeros = list()
for num in range(0, 5):
    numeros.append(int(input('Digite um número para adicionar na lista: ')))
print('='*30)
print(f'Sua lista ficou: {numeros}')
maior = max(numeros)
menor = min(numeros)

print(f'O maior número digitado foi o: {maior}, que se encontra na(s) posição(s): ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i} - ', end='')

print(f'\nO menor número digitado foi o: {menor}, que se encontra na(s) posição(s): ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i} - ', end='')

print('FIM!')