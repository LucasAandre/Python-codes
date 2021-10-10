#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTOS:
#- À vista DINHEIRO/CHEQUE: 10% de desconto
#- À vista no CARTÃO: 5% de desconto
#- Em até 2x NO CARTÃO: preço normal
#- 3x OU MAIS no cartão: 20% de juros

print('==== DESAFIO 44 ====\n\n')
print('Compras:\n')
produto = int(input('Por favor escolha um produto:\n1. Leite\n2. Refrigerante\n3. Água\n'))
if produto == 1:
    print('Leite:\n')
    valor = 2.30
    print('O Leite custa R$2.30')
    print('Selecione a forma de pagamento:')
    pag = int(input('1. À vista DINHEIRO\n2. À vista CHEQUE\n3. CARTÃO\n'))
    if pag == 1:
        print('À vista DINHEIRO (10% de desconto):\n')
        desconto = (valor*0.10)
        novo = (valor - desconto)
        print('O valor de R$2.30, com o desconto de 10% ficou em R${:.2f}'.format(novo))
        print('Obrigado e volte sempre!')
    elif pag == 2:
        print('À vista CHEQUE (10% de desconto):\n')
        desconto = (valor * 0.10)
        novo = (valor - desconto)
        print('O valor de R$2.30, com o desconto de 10%, ficou em R${:.2f}'.format(novo))
        print('Obrigado e volte sempre!')
    elif pag == 3:
        qntd = int(input('Em quantas vezes deseja realizar o pagamento?\n'))
        if qntd == 1:
            desconto = (valor*0.05)
            novo = (valor - desconto)
            print('O valor total a ser pago, com o desconto de 5%, ficou em R${:.2f}'.format(novo))
        elif qntd <= 2:
            print('O valor total a ser pago é de R$2.30')
        elif qntd >= 3:
            novo = (valor*1.20)
            print('O valor total a ser pago, com o juro de 20%, ficou em R${:.2f}'.format(novo))
elif produto == 2:
    print('Refrigerante:\n')
    valor = 5
    print('O Refrigerante custa R$5.00')
    print('Selecione a forma de pagamento:')
    pag = int(input('1. À vista DINHEIRO\n2. À vista CHEQUE\n3. CARTÃO\n'))
    if pag == 1:
        print('À vista DINHEIRO (10% de desconto):\n')
        desconto = (valor * 0.10)
        novo = (valor - desconto)
        print('O valor de R$5.00, com o desconto de 10% ficou em R${:.2f}'.format(novo))
        print('Obrigado e volte sempre!')
    elif pag == 2:
        print('À vista CHEQUE (10% de desconto):\n')
        desconto = (valor * 0.10)
        novo = (valor - desconto)
        print('O valor de R$5.00, com o desconto de 10%, ficou em R${:.2f}'.format(novo))
        print('Obrigado e volte sempre!')
    elif pag == 3:
        qntd = int(input('Em quantas vezes deseja realizar o pagamento?\n'))
        if qntd == 1:
            desconto = (valor * 0.05)
            novo = (valor - desconto)
            print('O valor total a ser pago, com o desconto de 5%, ficou em R${:.2f}'.format(novo))
        elif qntd <= 2:
            print('O valor total a ser pago é de R${:.2f}'.format(valor))
        elif qntd >= 3:
            novo = (valor * 1.20)
            print('O valor total a ser pago, com o juro de 20%, ficou em R${:.2f}'.format(novo))
elif produto == 3:
    print('Água:\n')
    valor = 3
    print('A Água custa R${:.2f}'.format(valor))
    print('Selecione a forma de pagamento:')
    pag = int(input('1. À vista DINHEIRO\n2. À vista CHEQUE\n3. CARTÃO\n'))
    if pag == 1:
        print('À vista DINHEIRO (10% de desconto):\n')
        desconto = (valor * 0.10)
        novo = (valor - desconto)
        print('O valor de R$3.00, com o desconto de 10% ficou em R${:.2f}'.format(novo))
        print('Obrigado e volte sempre!')
    elif pag == 2:
        print('À vista CHEQUE (10% de desconto):\n')
        desconto = (valor * 0.10)
        novo = (valor - desconto)
        print('O valor de R$3.00, com o desconto de 10%, ficou em R${:.2f}'.format(novo))
        print('Obrigado e volte sempre!')
    elif pag == 3:
        qntd = int(input('Em quantas vezes deseja realizar o pagamento?\n'))
        if qntd == 1:
            desconto = (valor * 0.05)
            novo = (valor - desconto)
            print('O valor total a ser pago, com o desconto de 5%, ficou em R${:.2f}'.format(novo))
        elif qntd <= 2:
            print('O valor total a ser pago é de R${:.2f}'.format(valor))
        elif qntd >= 3:
            novo = (valor * 1.20)
            print('O valor total a ser pago, com o juro de 20%, ficou em R${:.2f}'.format(novo))
else:
    print('Opção Inexistente!')
