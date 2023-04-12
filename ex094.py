'''Exercício Python 094: Crie um programa que leia 
nome, sexo e idade de várias pessoas, guardando os 
dados de cada pessoa em um dicionário e todos os 
dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

dados = dict()
todos = list()
soma = media = 0
while True:
    dados.clear()
    print('=-=' * 20)
    dados['nome'] = str(input('Digite o nome: '))
    
    while True:
        dados['sexo'] = str(input('Digite o sexo: [M/F] ')).upper()[0].strip()
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
            
    dados['idade'] = int(input(f'Digite a idade de {dados["nome"]}: '))
    
    soma += dados['idade']
    
    todos.append(dados.copy())
    
    print('=-=' * 20)
    resp = ' '
        
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    if resp == 'N':
        break
    
print('=-=' * 20)
print(f'A) Ao todo temos {len(todos)} pessoas cadastradas.')
media = soma / len(todos)
print(f'B) A média de idade cadastrada é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in todos:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=', ')
print()
print('D) Lista das pessoas que estão acima da média: ' , )
for p in todos:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print()
print('<<<  ENCERRADO  >>>')
