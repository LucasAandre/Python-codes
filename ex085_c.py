'''
085. Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
				DICA: Uma lista com duas listas alocadas (pares e ímpares)
'''

print('==== DESAFIO 85 ====\n')
print('Pares e Ímpares em Lista:\n\n')

from time import sleep

núm = [[], []]

for g in range(1, 8):
    valor = int(input(f'Digite o {g}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

núm[0].sort()
núm[1].sort()

print('=-'*30)
print(f'Os valores digitados foram: {núm}')
print(f'Os valores pares são: {núm[0]}')
print(f'Os valores ímpares são: {núm[1]}')

