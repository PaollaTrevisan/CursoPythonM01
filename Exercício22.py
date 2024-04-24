#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = str(input("Qual seu nome completo? "))
print('Seu nome em maiuscula é {}'.format(nome.upperr()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('O total de caracteres sem considerar os espaços é {}'.format(len(nome) - nome.count('    ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format)
