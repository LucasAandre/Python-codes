#Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
#valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles
#(desconsiderando o flag).
print('==== DESAFIO 66 ====\n')
print('Leitura de Valores Inteiros:\n\n')
cont = soma = num = 0
while True:
    num = int(input('Por favor digite um Valor Inteiro: '))

    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'A soma dos {cont} números digitados é igual a {soma}')
