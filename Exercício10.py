#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quanto em Real (R$) você possui?'))
print('O seu saldo em Real (R$) é R${} em dólar (US$) é US${}'.format(real, (real*5.09)))