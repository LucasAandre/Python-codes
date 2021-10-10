# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES. Se o valor
# digitado for ÍMPAR, desconsidere-o.

print('==== DESAFIO 50 ====\n')
print('Soma NÚMEROS PARES:\n\n')
soma = 0
for NEYMONSTRO in range(1, 7):
    a = int(input('Digite o {}º valor inteiro: '.format(NEYMONSTRO)))
    if a % 2 == 0:
        soma += a
print('A soma dos VALORES PARES digitados é: {}'.format(soma))
