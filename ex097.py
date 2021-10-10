'''
097. Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex: escreva('Olá, Mundo!')
Saída:
-----------
Olá, Mundo!
-----------

O número de linhas acompanha o tamanho da mensagem
'''

def escreva(txt):
    print('-'*cont)
    print(txt)
    print('-'*cont)

txt = str(input('Digite uma frase: '))
cont = len(txt)

escreva(txt)
