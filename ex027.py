# Faça um algoritmo que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

print(('='*4), 'DESAFIO 27', ('='*4))
NC = str(input('\n\nPor favor digite seu nome completo: ')).strip()
print('Analisando o nome {}...\n'.format(NC))
NND = NC.split()
print('Seu primeiro nome é: {}\nSeu último nome é: {}'.format((NND[0]), NND[-1]))



