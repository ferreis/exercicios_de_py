#Exe011 faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta nessesária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m^2
larg=float(input('Largura: '))
altu=float(input('Altura: '))
area=larg*altu
tint=area/2
print('largura: {:.2f} Altura {:.2f} Area: {:.2f}m² \nQuantidade de Tinta {:.2f}L '.format(larg,altu,area,tint))