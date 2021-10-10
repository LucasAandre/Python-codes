'''
104. Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um número')
'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um valor inteiro!')
        if ok:
            break
    return valor


#Programa Principal
n = leiaInt('Digite um valor inteiro: ')
print(f'Você digitou o valor {n}')
