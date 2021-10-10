#Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL. (Com WHILE e com FOR)
#Ex:
#5! = 5.4.3.2.1 = 120

print('==== DESAFIO 60 ====\n')
print('FATORIAL:\n\n')
num = float(input('Digite um número para descobrir seu fatorial: '))
c = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial))


