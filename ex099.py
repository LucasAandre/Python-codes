'''
099. Faça um programa que tenha uma função chamada maior(), que receba parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é maior.
'''

def maior():
    print('\n')
    print('-'*10)
    print(f'Os valores digitados foram: {lista}')
    lista.sort(reverse=True)
    print(f'Dentre os valores digitados, o maior é: {lista[0]}')
    print('-' * 10)


lista = list()
print('ANÁLISE DE VALORES\n')
while True:
    lista.append(int(input('Digite um valor inteiro: ')))
    resposta = str(input('Deseja continuar? [S/N]: ')).upper()
    if 'N' in resposta:
        break

maior()