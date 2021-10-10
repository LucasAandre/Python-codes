#Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA. No final, mostre os 10 primeiros termos dessa
#  progressão.

print('==== DESAFIO 51 ====\n')
print('Progressão Aritmética:\n\n')
a1 = int(input('Por favor digite o Primeiro Termo de uma P.A. (Progressão Aritmética): '))
a2 = int(input('Agora digite o Segundo Termo dessa P.A.: '))
r = (a2 - a1)
décimo = a1 + (10 - 1) * r # 10, pois quero o décimo termo
print('Os 10 Primeiros Termos dessa P.A. são:\n')
for c in range(a1, décimo + r, r):
    print(c, end= ' -> ')
print('ACABOU')

