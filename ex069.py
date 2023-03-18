'''Exercício Python 69: Crie um programa que leia a 
idade e o sexo de várias pessoas. A cada pessoa 
cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

cont18 = tot_homem = tot_mulher = 0 
while True:
    print('=-=' * 20)
    idade = int(input('Digite a idade: '))
        
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: ')).upper().strip()[0]
    
    if idade > 18:
        cont18 += 1
        
    if sexo == 'M':
        tot_homem +=1
    
    if sexo == 'F' and idade < 20:
        tot_mulher += 1
    
    print('=-=' * 20)        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print('=-=' * 20)    
print(f'O total de pessoas cadastrada com mais de 18 anos: {cont18}.')
print(f'O total de HOMENS cadastrados: {tot_homem}.')
print(f'O total de MULHERES cadastrados com MENOS de 20 anos: {tot_mulher}.')