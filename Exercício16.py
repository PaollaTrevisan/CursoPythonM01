#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
import math
num = float(input('Digite um número real:'))
print('O número real é {} e sua porção inteira {}'.format(num, math.trunc(num)))