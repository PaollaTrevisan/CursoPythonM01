#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
x = input(print('Digite qualquer coisa:'))
print('O tipo primitivo é:', type(x))
print('É um número?', x.isnumeric())
print('Tem somente espaços?', x.isspace())
print('É um número ou uma letra?', x.isalpha())
print(x.isdigit())
print(x.isdecimal())