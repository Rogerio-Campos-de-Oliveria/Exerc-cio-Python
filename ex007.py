'''Exercício Python 007: Desenvolva um programa que
leia as duas notas de um aluno, calcule e mostre a sua média.'''

nota_01 = nota_02 = total = média = 0
nome_aluno = str(input('Escreva o nome do aluno: '))
nota_01 = float(input(f'Digite a nota do aluno {nome_aluno}: '))
nota_02 = float(input(f'Digite a outra nota do aluno {nome_aluno}: '))
total = nota_01 + nota_02
média = total / 2
print(
    f'As notas do aluno {nome_aluno} foram {nota_01:.2f} e {nota_02:.2f} e sua média é {média:.2f}.')
