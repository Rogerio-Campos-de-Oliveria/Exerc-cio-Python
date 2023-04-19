'''Exercício Python 105: Faça um programa que tenha uma 
função notas() que pode receber várias notas de alunos 
e vai retornar um dicionário com as seguintes 
informações:

– Quantidade de notas 
– A maior nota
– A menor nota  
– A média da turma
– A situação (opcional) ''' 

def notas(dados):
    print(f'A maior nota é {max(dados)}')
    print(f'A maior nota é {min(dados)}')
    média = sum(dados) / len(dados)
    print(f'A média nota é {média}')
    
    if média >= 7:
        print(f'A situação do aluno é APROVADO.')
    elif média <= 5:
        print(f'A situação do aluno é REPROVADO.')
    elif 5.1 <= média <= 6.9:
        print(f'A situação do aluno é RECUPERAÇÃO.')
    
    
    
#Principal Programa

lista = list()

resp = ''
while True:
    n = float(input('Digite a nota do aluno: '))
    resp = str(input('Deseja digitar uma nova nota? [S/N] ')).upper()[0].strip()
    if resp not in 'SN':
        resp = str(input('ERRO! Deseja digitar uma nova nota? [S/N] ')).upper()[0].strip()
    
    lista.append(n)
    
    if resp == 'N':
        break
    

print(notas(lista))
