'''Exercício Python 085: Crie um programa onde o 
usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados 
os valores pares e ímpares. No final, mostre os valores 
pares e ímpares em ordem crescente.'''

lista = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}° valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('=-=' * 20)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}.')
print(f'Os valores ímpares digitados foram: {lista[1]}.')
