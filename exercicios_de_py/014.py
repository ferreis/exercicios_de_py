#Exe014 Escreva um programa que converta uma temperatura digitada em °c e converta para °f
c =float(input('Digite a Temperatura celsius: '))
f=c*9/5+32
print('a temperatura {:.1f}°c fica {:.1f}°f'.format(c, f))