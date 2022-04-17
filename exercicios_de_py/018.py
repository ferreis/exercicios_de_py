#Exe018 faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians,sin,cos,tan
ang = float(input('Digite o ângulo que deseja: '))
senang = sin(radians(ang))
cosang = cos(radians(ang))
tangang = tan(radians(ang))
print('Seno: {:.2f}\nCosseno: {:.2f}\ntangente: {:.2f}'.format(senang,cosang,tangang))