#Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL. (Com WHILE e com FOR)
#Ex:
#5! = 5.4.3.2.1 = 120

print('==== DESAFIO 60B ====\n')
print('Fatorial:\n\n')
num = int(input('Digite um número para descobrir seu FATORIAL: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
