#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe seu salário: R$'))
print('Antes o seu salário é:{} com o aumento de 15% passou a ser:{}'.format(salario, (salario+salario*15/100)))