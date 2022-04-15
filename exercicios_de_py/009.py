#Exe009 faça um programa que leia um númeiro inteiro qualquer e mostre na tela a sua tabuada
n=int(input('Digite um numero inteiro: '))
for cont in range(10):
    print('{} x {} = {}'.format(n,cont+1,n*(cont+1)))
#agora como o exe009 realmente quer
print('{:=^20}'.format(n))
print('{} x 1= {}'.format(n,n))
print('{} x 2= {}'.format(n,n*2))
print('{} x 3= {}'.format(n,n*3))
print('{} x 4= {}'.format(n,n*4))
print('{} x 5= {}'.format(n,n*5))
print('{} x 6= {}'.format(n,n*6))
print('{} x 7= {}'.format(n,n*7))
print('{} x 8= {}'.format(n,n*8))
print('{} x 9= {}'.format(n,n*9))
print('{} x 10= {}'.format(n,n*10))
