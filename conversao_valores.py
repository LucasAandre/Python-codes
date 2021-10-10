#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
#- 1 para BINÁRIO
#- 2 para OCTAL
#- 3 para HEXADECIMAL

print('==== DESAFIO 37 ====\n\n')
print('BASE DE CONVERSÃO:\n')
inteiro = int(input('Por favor digite um Número Inteiro: '))
escolha = int(input('Deseja converter esse valor para:\nDigite:\n1. Para BINÁRIO\n2. Para OCTAL\n3. para HEXADECIMAL\n '))
if escolha == 1:
    binario = bin(inteiro)[2:]
    print('O número {} convertido para um valor Binário fica: {}'.format(inteiro, binario))
elif escolha == 2:
    octal = oct(inteiro)[2:]
    print('O número {} convertido para um valor Octal fica: {}'.format(inteiro, octal))
elif escolha == 3:
    hexadecimal = hex(inteiro)[2:]
    print('O número {} convertido para um valor Hexadecimal fica: {}'.format(inteiro, hexadecimal))
else:
    print('Essa opção não existe. Tente novamente.')

#Fatiei os valores finais, pois as 2 primeiras casas da string são desnecessárias. Ex: 0b / 0o / 0x
