# Crie um algoritmo que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

print('==== DESAFIO 25 ====\n\n')
Melo = str(input('Por gentileza digite seu nome completo: ')).strip()
MeloMesmo = Melo.upper()
print('Analisando o nome {}...\n'.format(Melo))
print('Existe Silva em seu nome: {}'.format('SILVA' in MeloMesmo.split()))
