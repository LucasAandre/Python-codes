#064. Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar
#o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles
#(desconsiderando o flag - 999).
print('==== DESAFIO 64 ====\n\n')
cont = n = soma = 0
n = int(input('Digite um valor inteiro [999 para encerrar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor inteiro [999 para encerrar]: '))
print('Você digitou {} valores e a soma geral é igual a {}'.format(cont, soma))
