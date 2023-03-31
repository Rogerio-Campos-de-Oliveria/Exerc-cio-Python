'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados. 
B) A soma dos valores da terceira coluna. 
C) O maior valor da segunda linha.

''' 

matriz = [[0,0,0], [0,0,0,], [0,0,0]]
somaPar = maior_numero = somaCaoluna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
print('=-=' * 20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()
print('=-=' * 20)    
print(f'A soma dos valores pares é {somaPar}.')

for l in range(0, 3):
    somaCaoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somaCaoluna}.')

for c in range(0,3):
    if c == 0:
        maior_numero = matriz[1][c]
    elif matriz[1][c] > maior_numero:
        maior_numero = matriz[1][c]
print(f'O valor maior da segunda linha é {maior_numero}.')

print('=-=' * 20)