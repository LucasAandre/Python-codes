# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
print(('='*4), 'DESAFIO 40', ('='*4), '\n\n')
print('Menção Final:\n')
nota1 = float(input('Digite a 1º Nota do Aluno: '))
nota2 = float(input('Digite a 2º Nota do Aluno: '))
media = ((nota1 + nota2) / 2)
print('A média do Aluno é: {:.1f}'.format(media))
if media < 5:
    print('ALUNO REPROVADO')
elif media == 5 or media < 7:
    print('ALUNO DE RECUPERAÇÃO')
elif media >= 7:
    print('ALUNO APROVADO')


