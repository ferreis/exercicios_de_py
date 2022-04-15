#Exe013 Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=float(input('Seu Salario: '))
aumento=salario*0.15 
novo_salario=salario+aumento
#ou novo_salario=salario*1.15 vai dar o mesmo resultado no final talvez seja mais pratico?...
print('Seu salário de R${:.2f} ira ter um aumento de 15% que e R${:.2f}, seu novo salario sera de R${:.2f}'.format(salario,aumento,novo_salario))

