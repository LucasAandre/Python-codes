# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

'''Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência:
 Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
 outros dois e maior que o valor absoluto da diferença entre essas medidas'''

print('==== DESAFIO 35 ====\n')
reta1 = float(input('Por favor digite a medida da primeira reta: '))
reta2 = float(input('Agora digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))
if (reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2)):
    ehTriangulo = True
else:
    ehTriangulo = False

if (ehTriangulo):
    print('Os valores formam um triângulo:')
    if (reta1 == reta2 == reta3):
        print('Triângulo Equilátero')
    elif (reta1 == reta2 != reta3) or (reta1 == reta3 != reta2) or (reta2 == reta3 != reta1):
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Essas retas não formam um triângulo')
