# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
#  que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
print('==== DESAFIO 20 ====\n')
print('Ordem dos Alunos:\n')
Aluno1 = input('1º Aluno: ')
Aluno2 = input('2º Aluno: ')
Aluno3 = input('3º Aluno: ')
Aluno4 = input('4º Aluno: ')
lista = [Aluno1, Aluno2, Aluno3, Aluno4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
