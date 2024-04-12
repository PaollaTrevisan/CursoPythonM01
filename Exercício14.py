#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperatura = float(input('Qual a temperatura?'))
print('A temperatura informada foi {} Cº é {}Fº'.format(temperatura,(temperatura * 9/5)+32))