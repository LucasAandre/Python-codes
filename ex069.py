#Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada, o programa deverá perguntar
#se o USUÁRIO quer ou não continuar. No final, mostre:
#(a)Quantos pessoas tem mais de 18 anos.
#(b)Quantos homens foram cadastrados.
#(c)Quantas mulheres tem menos de 20 anos.
print('==== DESAFIO 69 ====\n')
print('CADASTRO NELVIS:\n\n')
print('-'*30)
maiores = 0
masc = 0
menores = 0
while True:
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Agora digite seu sexo [M/F]: ')).upper()
    if idade > 18:
        maiores += 1
    escolha = str(input('Deseja continuar com os cadastros? [S/N]: ')).upper().strip()
    if sexo in 'M':
        masc += 1
    elif sexo in 'F':
        if idade < 20:
            menores += 1
    if escolha in 'N':
        break
print('-'*30)
print('FIM DOS CADASTROS!')
print(f'Dos cadastrados, {maiores} têm mais de 18 anos.')
print(f'{masc} homens foras cadastrados.')
print(f'E {menores} mulheres tem menos de 20 anos.')
