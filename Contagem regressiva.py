# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 ATÉ 0,
#  com uma pausa de 1 SEGUNDO entre eles.

from time import sleep
import emoji
print('==== DESAFIO 46 ====\n')
print('Queima de Fogos de Artifício:\n\n')
escolha = int(input('''Você deseja ver a Contagem Regressiva para o Ano Novo?
        [1] SIM
        [2] NÃO\n'''))
if escolha == 1:
    print('Contagem Regressiva para o ANO NOVO:\n')
    for fogos in range(10, -1, -1):
        print(fogos)
        sleep(1)
    print('FELIZ ANO NOVO!!!!')
elif escolha == 2:
    print(emoji.emojize('Você não verá a contagem regressiva para os Fogos de Artifício, mas em breve o show irá começar :wink:', use_aliases=True))
else:
    print('Opção Inexistente!')
