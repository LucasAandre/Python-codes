#Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso lidos.

print('==== DESAFIO 55 ====\n')
print('MAIOR e MENOR peso lido:\n\n')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\nO maior peso lido foi de {}KG'.format(maior))
print('O menor peso lido foi de {}KG'.format(menor))
