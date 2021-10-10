'''
077. Crie um programa que tenha uma TUPLA com VÁRIAS PALAVRAS (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são as suas VOGAIS.
'''
print('='*4, 'DESAFIO 77', '='*4, '\n')
'''teste0 = int(input('Digite 3 valores inteiros: '))
teste1 = int(input(''))
teste2 = int(input(''))

print(teste0, teste1, teste2)
'''
print('Vogais em Palavras:\n\n')

palavras = ('CLARO', 'SUITE', 'PYTHON', 'C', 'JAVA', 'ENGENHARIA', 'ELETRICA', 'SOFTWARE', 'NOTEBOOK', 'SANTOS',
            'PARANOX', 'PARA', 'PHP', 'HTML', 'IHM', 'LADDER', 'ARDUINO', 'PROGRAMAÇAO', 'MATEMATICA', 'EXATAS')

for palavra in palavras:
    print(f'As vogais em {palavra} são: ', end=' ')
    for letra in range(0, len(palavra)):
        if palavra[letra] == 'A' or palavra[letra] == 'E' or palavra[letra] == 'I' or palavra[letra] == 'O' or palavra[letra] == 'U':
            print(f'{palavra[letra]}', end=' ')
        print()


