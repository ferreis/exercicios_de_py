#Exe017 Faça um programa que leia o comprimento do cateto opostoe do cateto adjacente de um triângulo, calcule e mostre o comprimento 
#da hipotenusa.

import math

cato = float(input('Valor do Cateto oposto '))
cata = float(input('Valor do cateto adjacente '))
hipo = (cato**2+cata**2)**(1/2) #ou 0.5 
# ou 
ou_hipo = math.sqrt(pow(cato,2) + pow(cata,2))
# ou ainda mais facil
fouhipo = math.hypot(cato, cata)
print('O comprimento da Hipotenusa: {:.2f}.\nou: {:.2f} | {:.2f}'.format(hipo,ou_hipo,fouhipo))