'''Exercício Python 040: Crie um programa que leia 
duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a 
média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print(f'Sua média foi de {média:.2f}')
if média > 7:
    print('PARABÉNS !!!! Você foi aprovado!')
elif 5 <= média < 7:
    print('RECUPERAÇÃO!!! Você precisa melhorar.')
elif média <= 4.99:
    print('REPROVADO!!! Você não atingiu a nota.')
