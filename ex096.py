'''
096. Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''

def área(l, c):
    a = (l*c)
    print(f'Sendo {l} m de largura e {c} m de comprimento, a área total desse terreno é: {a} m²')


l = float(input('Digite a largura do terreno [m]: '))
c = float(input('Digite o comprimento do terreno [m]: '))

área(l,c)