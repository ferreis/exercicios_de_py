#Exe008 Escreva um programa que leia um valor em metros e o exiba convertido em CENTIMETROS e milímetros

metros=float(input('Digite quantos Metros quer converter em CM e MM: '))
cm=metros*100
mm=cm*10
print('Seu {}m fica em CM e MM \nCM: {}\nMM: {}'.format(metros,cm,mm))