#Exe006 Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n=float(input('Digite um número: '))
print('Seu Dobro: {} \nSeu triplo: {} \nRaiz quadrada: {}'.format(n*2,n*3,n**(1/2)))
#posso guarda essa info ou so  mostrar na tela...
print('{:=^20}'.format(n))
n2=n*2
n3=n*3
nrq=n**(1/2)
print('Seu Dobro: {} \nSeu triplo: {} \nRaiz quadrada: {:.2f}'.format(n2,n3,nrq))