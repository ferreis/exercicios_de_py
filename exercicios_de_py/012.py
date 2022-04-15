#Exe012 faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco=float(input('Preço do Produto: '))
print("Novo Preço com 5% de desconto ja incluido: R${:.2f}".format(preco*0.95))
#ou Guardando a info do desconto
print('-------------------------------')
desc=preco*.95
print('Novo preço comm 5% de desconto ja incluido R${:.2f}'.format(desc))