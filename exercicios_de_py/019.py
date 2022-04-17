#Exe019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
nome1 = input('1° Aluno: ')
nome2 = input('2° Aluno: ')
nome3 = input('3° Aluno: ')
nome4 = input('4° Aluno: ')
lista = [nome1,nome2,nome3,nome4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))