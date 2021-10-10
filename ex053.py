#Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.

print('==== DESAFIO 53 ====\n')
print('É Polídromo ou não é?\n\n')
frase = str(input('Digite uma frase (desconsiderando acentos): ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras) #Elimina os espaços entre as palavras. '*'.join colocaria um * no lugar dos espaços entre as palavras
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}\n'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
