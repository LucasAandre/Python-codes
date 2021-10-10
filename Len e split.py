# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas;
# > O nome com todas as letras minúsculas;
# > Quantas letras no geral (sem contar os espaços)
# > Quantas letras tem o primeiro nome.

print('==== DESAFIO 22 ====\n\n')
#print('Nome:\n')
nome = str(input('Por favor digite seu nome completo: ')).strip()# Eliminei os espaçoes desnecessários
print('Seu nome completo com todas as letras maiúsculas fica: {}'.format(nome.upper()))
print('Com todas as letras minúsculas fica: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))





