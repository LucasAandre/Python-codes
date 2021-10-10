#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.

from time import sleep
from datetime import date
print('==== DESAFIO 39 ====\n\n')
print('Verificando o Alistamento:\n')
atual = date.today().year
sexo = str(input('Qual o seu sexo?\n[M] - Masculino\n[F] - Feminino\n')).upper()
nascimento = int(input('Ano de Nascimento: '))
idade = (atual - nascimento)
if sexo == 'M':
    if idade == 18:
         print('Você tem 18 anos e está na hora de se alistar no Serviço Militar.')
    elif idade > 18:
        print('Você tem {} anos e devia ter se alistado no Serviço Militar com 18 anos.'.format(idade))
    else:
        print('Você tem {} anos e deve se alistar no Serviço Militar com 18 anos.'.format(idade))
elif sexo == 'F':
    print('O alistamento no Serviço Militar não é obrigatório para mulheres.')

else:
    print('Opção Inexistente! Tente Novamente.')
escolha = str(input('Sendo mulher, deseja, mesmo assim, se alistar?\n[SIM] ou [NÃO]\n')).upper()
if escolha == 'SIM':
    if idade == 18:
        print('Você tem 18 anos e está na hora de se alistar no Serviço Militar.')
    elif idade > 18:
        print('Você tem {} anos e devia ter se alistado no Serviço Militar com 18 anos.'.format(idade))
    else:
        print('Você tem {} anos e deve se alistar no Serviço Militar com 18 anos.'.format(idade))
elif escolha == 'NÃO':
    print('Tudo bem. Indique esse programa para um amigo!')
sleep(10)
