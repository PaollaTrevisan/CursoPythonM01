# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
n1 = str(input('primeiro nome'))
n2 = str(input('segundo nome'))
n3 = str(input('terceiro nome'))
n4 = str(input('quarto nome'))
lista =[n1, n2, n3, n4]
sorteio = random.choice(lista)
print('O nome escolhido é: {}'.format(sorteio))