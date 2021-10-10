#Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os
#valores e qual foi o MAIOR e o MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não CONTINUAR
#a digitar valores.
print('==== DESAFIO 65 ====\n\n')
MaiorNum = MenorNum =cont = soma = num = 0
escolha = 'S'
while escolha in 'Ss':
    num = int(input('Digite um valor inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        MaiorNum = MenorNum = num
    else:

        if num > MaiorNum:
            MaiorNum = num
        elif num < MenorNum:
            MenorNum = num
    escolha = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} valores e a MÉDIA é igual a {}'.format(cont, media))
print('O MENOR número digitado foi {} e o MAIOR foi {}'.format(MenorNum, MaiorNum))
