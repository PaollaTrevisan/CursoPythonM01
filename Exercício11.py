#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('Qual a altura?'))
largura = float(input('Qual a largura?'))
print("Altura:{}; Largura:{}; Área total:{} m2".format(altura, largura, (largura*altura)**2))
    
    
