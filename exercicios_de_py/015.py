#Exe015 Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por kmm rodado

dia = int(input('Quantos dias o carro foi alugado? '))
km_rodado = float(input('Quantos Km rodados? '))
valor_dia = dia * 60
valor_km = km_rodado * 0.15
valor_total = valor_dia + valor_km
print('O carro voi Alugado por {} Dias no valor de R${:.2f}, e rodou por {} Km somando no valor de R${:.2f}\n Total do aluguel R${:.2f}'.format(dia,valor_dia,km_rodado,valor_km,valor_total))