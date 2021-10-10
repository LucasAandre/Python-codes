# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

print('==== DESAFIO 24 ====\n\n')
Nome = str(input('Por favor digite o nome completo de sua cidade: ')).strip()
NovoNome = Nome.capitalize()
separa = NovoNome.split()
print('Analisando o nome {}...'.format(Nome))
print('O nome de sua cidade começa com Santo: ')
print('Santo' in separa[0])

