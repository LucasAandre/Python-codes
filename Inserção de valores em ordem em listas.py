'''
Crie um programa onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os em uma lista, JÁ NA POSIÇÃO CORRETA
de inserção (sem usar o SORT()). No final, mostre a LISTA ORDENADA na tela.
'''

print('==== DESAFIO 80 ====\n')
print('Na ordem sem SORT():\n\n')

lista = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('='*30)
print(f'A lista em ordem fica: {lista}')

