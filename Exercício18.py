#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = float(input('Qual o angulo? '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O seno de {} é {:.2f}'.format(angulo, seno))
print('O cosseno de {} é {:.2f}'.format(angulo, cos))
print('A tangente de {} é {:.2f}'.format(angulo, tan))