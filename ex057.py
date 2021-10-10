#Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

print('==== DESAFIO 57 ====\n')
print('Validação de Dados:\n\n')
sexo = str(input('Por favor digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor digite seu sexo novamente: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso.')
elif sexo == 'F':
    print('Sexo Feminino registrado com sucesso.')
