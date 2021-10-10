'''
Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA.
'''

print('=== DESAFIO 83 ====\n')
print('Análise de Expressões:\n\n')

exp = str(input('Digite uma expressão: '))
estoque = []


#Resolução Guanabara:
for símb in exp:
    if símb == '(':
        estoque.append(símb)
    elif símb == ')':
        if len(estoque) > 0:
            estoque.pop()
        else:
            estoque.append(símb)
            break
print('='*30)
if len(estoque) == 0:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')


#Minha Resolução:
'''
aberto = 0
fechado = 0

for símb in exp:
    if símb == '(':
        aberto += 1
    elif símb == ')':
        if aberto == 0:
            fechado += 1
            break
        else:
            fechado += 1
print('='*30)
if aberto == fechado:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')
'''
