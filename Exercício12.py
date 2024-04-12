#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Qual o valor do produto?'))
print('O valor do produto é R${}, o valor com 5% de desconto é R${}'.format(produto, (produto - produto*5/100)))