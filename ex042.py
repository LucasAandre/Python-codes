#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: todos os lados iguais
#- Isósceles: dois lados iguais
#- Escaleno: todos os lados diferentes

'''Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência:
 Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
 outros dois e maior que o valor absoluto da diferença entre essas medidas'''

print('==== DESAFIO 42 ====\n\n')
print('Verificando Triângulos:\n')
lado1 = float(input('Digite a medida da 1º Reta em Centímetros: '))
lado2 = float(input('Digite a medida da 2º Reta em Centímetros: '))
lado3 = float(input('Digite a medida da 3º Reta em Centímetros: '))
if ((lado1 + lado2) > lado3 and ((lado1 + lado3) > lado2) and (lado2 + lado3) > lado1):
    ETriangulo = True
else:
    ETriangulo = False

if ETriangulo:
    print('Essas retas formam um triângulo ', end='')
    if (lado1 == lado2 == lado3):
        print('EQUILÁTERO.')
    elif (lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1):
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Essas retas não formam um triângulo.')

#Um "if" dentro de outro "if": Condição Aninhada