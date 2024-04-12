#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite um valor em metros (M):'))
print('Metros:{}, Centímetros:{}, Milímetros:{}'.format(n, (n*10), (n*10**2)))