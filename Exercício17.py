#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
catetoAdjacente = float(input("Qual o valor do cateto adjacente? "))
catetoOposto = float(input('Qual o valor do cateto oposto? '))
hipotenusa = (catetoAdjacente**2 + catetoOposto**2) / 2
print('O valor dos catetos são: Adjacente {}. Oposto {}'.format(catetoAdjacente, catetoOposto))
print('O valor da Hipotenusa: {}'.format(hipotenusa))