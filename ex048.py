# Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram no
#  intervalo de 1 até 500.

print('==== DESAFIO 48 ====\n')
print('Ímpares e Múltiplos de 3 entre 01 e 500\n\n')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # cont += 1
        soma = soma + c # soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
