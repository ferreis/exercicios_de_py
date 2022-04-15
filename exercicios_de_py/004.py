#Exe004 Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('Digite algo: ')
#no teste sempre colocar o tipo primitivo na frente, se não vai ser sempre STR
print(type(a))
print('tem espaço? ',a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabético? ',a.isalpha())
print('É alfanúmerico? ',a.isalnum())
print('Está em maiúscula? ',a.isupper())
print('Está em minúscula? ',a.islower())
print('Está capitalizado? ', a.istitle())
print('------------------------------------------------')
#a outra forma de fazer isso com o .format()
print('tem espaço? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanúmerico? {}'.format(a.isalnum()))
print('Está em maiúscula? {}'.format(a.isupper()))
print('Está em minúscula? {}'.format(a.islower()))
print('Está capitalizado? {}'.format(a.istitle()))

