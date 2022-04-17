#Exe016 Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção interira
from math import trunc

num = float(input('Digite umm número: '))
inum = trunc(num)
print('Seu numero real é {}, e no inteiro é {} '.format(num, inum))
# ou 
print('Seu numero real é {}, e no inteiro é {} '.format(num, int(num)))