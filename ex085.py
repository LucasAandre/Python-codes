'''
085. Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
				DICA: Uma lista com duas listas alocadas (pares e ímpares)
'''

#Está incorreto, pois uso listas separadas e o exercício pede uma lista só.
#Resolução correta em ex085_C.py

print('==== DESAFIO 85 ====\n')
print('Pares e Ímpares em Lista:\n\n')

from time import sleep
valores = list()
dados = []
pares = []
ímpares = []
#oficial =  list()

for c in range(0, 7):
    dados.append(int(input(f'Digite o {c+1}º valor: ')))
    if dados[c] % 2 == 0:
        pares.append(dados[c])
        sleep(1)
        print('Valor PAR adicionado com sucesso!')
    else:
        ímpares.append(dados[c])
        sleep(1)
        print('Valor ÍMPAR adicionado com sucesso!')

valores.append(pares[:])
valores.append(ímpares[:])
#oficial.append(valores)
dados.clear()
pares.sort()
ímpares.sort()

print('=-'*30)
print(f'Sua lista completa é: {valores}')
print(f'Os valores pares são: {pares}')
print(f'Os valores ímpares são: {ímpares}')
