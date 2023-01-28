"""Exercício Python 004: Faça um programa que leia
algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele."""

texto = input('Digite o que você quer: ')
print()
print(f'O tipo primitivo desse valor é ', type(texto))
print(f'Só tem espaços? ', texto.isspace())
print('É um número? ', texto.isnumeric())
print('É alfabético? ', texto.isalpha())
print('É alfanumérico? ', texto.isalnum())
print('Está em maiúculo? ',texto.isupper())
print('Está em minúsculo? ', texto.islower())
