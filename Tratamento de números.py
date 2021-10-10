# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

print('==== DESAFIO 23 ====\n\n')
valor = int(input('Por favor digite um número de 0 a 9999: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(u, d, c, m))
