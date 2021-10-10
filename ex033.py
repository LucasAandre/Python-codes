# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

print('==== DESAFIO 33 ====\n')
a = float(input('Por favor digite o primeiro número: '))
b = float(input('Agora digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
if c > maior:
    maior = c
else:
    maior = maior
if c < menor:
    menor = c
else:
    menor = menor
print('O maior número digitado foi: {}\nJá o menor foi: {}'.format(maior, menor))
