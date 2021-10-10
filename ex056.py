#Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre:
#- A MÉDIA DE IDADE do grupo;
#- Qual é o nome do homem MAIS VELHO;
#- Quantas mulheres têm MENOS DE 20 anos.

print('==== DESAFIO 56 ====\n')
print('Analisador Completo:\n\n')
somaidade = 0
mediaidade = 0
idadehomemvelho = 0
nomevelho = ''
numeromulhernova = 0
for l in range(1, 5):
    print('------ {}º Pessoa ------'.format(l))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if l == 1 and sexo in 'Mm':
        idadehomemvelho = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        numeromulhernova += 1
mediaidade = somaidade / 4
print('\nA média de idade do grupo é de {} anos'.format(mediaidade))
print('{} tem {} anos e é o homem mais velho do grupo'.format(nomevelho, idadehomemvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(numeromulhernova))
