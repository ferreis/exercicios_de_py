#Exe010 crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$1.00 = R$3.27

d=float(input('Quanto R$ voce tem na carteira: '))
print('Você pode Comprar US${:.2f}'.format(d/3.27))