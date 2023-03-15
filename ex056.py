'''Exercício Python 56: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: a média 
de idade do grupo, qual é o nome do homem mais velho e quantas 
mulheres têm menos de 20 anos.'''


soma_idade = média_idade = maio_idade_homem = tot_mulher20 = 0
nome_velho = ''
print('=' * 20)
for c in range(1, 5):
    nome = str(input(f'Digite o {c}° nome: ')).strip()
    idade = int(input(f'Digite a idade do {nome}: '))
    sexo = str(input('Digite o sexo [M / F]: ')).strip().upper()
    print('=' * 20)
    soma_idade += idade
    if c == 1 and sexo == 'M':
        maio_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade >  maio_idade_homem:
        maio_idade_homem = idade
        nome_velho = nome       
    if sexo in 'Ff' and idade < 20:
        tot_mulher20 +=1
média_idade = soma_idade / 4
print(f'A média de idade do grupo é de {média_idade:.2f} anos.') 
print(f'O homem mais velho {maio_idade_homem} anos e se chama {nome_velho}.')
if tot_mulher20 == 0:
    print(f'Não temos nenhuma mulher com idade abaixo de 20 anos.')
else:
    print(f'Ao todo são {tot_mulher20} mulheres com menos de 20 anos.')