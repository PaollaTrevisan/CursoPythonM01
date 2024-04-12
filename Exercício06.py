#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
n = int(input(print('Escolha um número inteiro (sem vírgula): ')))
print('O número escolhido foi {}, o seu dobro {}, seu triplo {} e a sua raiz quadrada {}'.format(n, (n*2), (n*3), (math.sqrt(n))))