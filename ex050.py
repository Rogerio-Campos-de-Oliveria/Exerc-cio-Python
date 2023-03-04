'''Exercício Python 50: Desenvolva um programa que 
leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado for 
ímpar, desconsidere-o.'''

s = cont = 0
for c in range(0, 6):
    número = float(input('Digite um valor que deseja: '))
    if número % 2 == 0:
        s += número
        cont += 1
print(f'Você informou {cont} números PARES e soma foi {s:.0f}.')
