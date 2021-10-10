# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "a";
# > Em que posição ela aparece a primeira vez; (letra a)   #Talvez l
# > Em que posição ela aparece pela última vez. (letra a)  #Talvez r

print('==== DESAFIO 26 ====\n\n')
frase = str(input('Por favor digite uma frase qualquer: ')).strip()
NewFrase = frase.lower()
print('\nAnalisando a frase {}...\n'.format(frase))
print('Essa frase possui {} letras A(s)'.format(NewFrase.count('a')))
primeira = NewFrase.find('a') + 1# Para o usuário entender melhor (POSIÇÃO 1 É MAIS VIÁVEL DO QUE POSIÇÃO 0)
última = NewFrase.rfind('a') + 1
print('Sendo que a primeira aparece na {}º posição e a última aparece na {}º posição'.format(primeira, última))

