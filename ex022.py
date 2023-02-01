'''Exercício Python 22: Crie um programa que leia o nome 
completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculo é {nome.upper()}.')
print(f'Seu nome em minúsculo é {nome.lower()}.')
print(f'Seu nome tem ao todo {(len(nome) - nome.count(" "))} letras.')#não esquecer de usar aspas duplas quando for colocar aspas dentro de outra para diferenciar.
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')#não esquecer de usar aspas duplas quando for colocar aspas dentro de outra para diferenciar.
