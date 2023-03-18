'''Exercício Python 65: Crie um programa que leia 
vários números inteiros pelo teclado. No final da 
execução, mostre a média entre todos os valores e qual 
foi o maior e o menor valores lidos. O programa deve 
perguntar ao usuário se ele quer ou não continuar a 
digitar valores.'''

resp = 'S'
tot = quant = media = maior = menor = 0
while resp in 'S':
    núm = int(input('Digite um valor inteiro: '))
    tot += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < núm:
            menor = núm
    
    resp = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
media = tot / quant
print(f'Você digitou {quant} número e a média foi {media:.2f}.')
print(f'O número maior digitado foi {maior}.')
print(f'O número menor digitado foi {menor}.')
