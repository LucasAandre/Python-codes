# Crie um algoritmo que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

print('==== DESAFIO 25 ====\n\n')
MeloGayMesmo = str(input('Por gentileza digite seu nome completo: ')).strip()
MeloMuitoGayMesmo = MeloGayMesmo.upper()
print('Analisando o nome {}...\n'.format(MeloGayMesmo))
print('Existe Silva em seu nome: {}'.format('SILVA' in MeloMuitoGayMesmo.split()))
#print('Silva' in MeloGayMesmo)

#nome = input('Digite seu nome: ').upper()
#print('SILVA' in nome.split())