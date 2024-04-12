#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
print('As suas notas são {} e {}. Sua média final é {}'.format(nota1, nota2, (nota1+nota2)/2))