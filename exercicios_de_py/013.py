#Exe013 Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=float(input('Seu Salario: '))
aumento=salario*0.15
novo_salario=salario+aumento
print('Seu salário de R${} ira ter um aumento de 15% que e R${}, seu novo salario sera de R${}'.format(salario,aumento,novo_salario))