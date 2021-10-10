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


#x = 15 % 100
#print(x)
'''print('=== LEITOR DE NÚMEROS ATÉ 9999 ===')
n = int(input('Digite um número até 9999: '))
print('== MÉTODO INT ==')
print('Unidade = {}'.format(n % 10))
print('Dezena = {}'.format((n // 10) % 10))
print('Centena = {}'.format((n // 100) % 10))
print('Milhar = {}'.format(n // 1000))
print('== MÉTODO STRING ==')
n = '000' + str(n)  # para que possamos escrever 1, 23 ou 395 #Não deu certo comigo
print('Unidade = {}'.format(n[-1]))  # Também daria pra usar n[len(n)-1]
print('Dezena = {}'.format(n[-2]))
print('Centena = {}'.format(n[-3]))
print('Milhar = {}'.format(n[-4]))'''
