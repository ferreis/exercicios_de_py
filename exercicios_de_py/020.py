#Exe020 O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('1° Aluno: '))
n2 = str(input('2° Aluno: '))
n3 = str(input('3° Aluno: '))
n4 = str(input('4° Aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
#Minha resposta
ordem = 1
print('A ordem dos Alunos para Apresentação:')
for x in lista:
    print('{}°{}'.format(ordem, x))
    ordem+=1
print('--------------------------------------------------')
#Outra resposta
print('A ordem dos Alunos para Apresentação:\n{}'.format(lista))