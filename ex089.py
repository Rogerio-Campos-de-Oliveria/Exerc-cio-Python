'''Exercício Python 089: Crie um programa que leia nome 
e duas notas de vários alunos e guarde tudo em uma 
lista composta. No final, mostre um boletim contendo a 
média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.'''

from time import sleep
cadastro = []


while True:
    nome_aluno = str(input('Digite o nome do aluno: '))
    nota_01 = float(input(f'Digite a primeira nota do {nome_aluno}: '))
    nota_02 = float(input(f'Digite a segunda nota do {nome_aluno}: '))
    média = (nota_01 + nota_02) / 2
    cadastro.append([nome_aluno, [nota_01, nota_02], média])
    

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('=-=' * 20)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-=' * 20)

for i, v in enumerate(cadastro):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')

while True:
    print('=-=' * 20)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        sleep(1.5)
        break
    if opc <= len(cadastro) - 1:
        print(f'Notas de {cadastro[opc][0]} são {cadastro[opc][1]}.')
print('<<< VOLTE SEMPRE >>>')
