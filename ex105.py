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
    """_Função para analisar notas e situação de vários alunos_

    Args:
        dados (_type_): _Um ou mais notas dos alunos (aceita várias_
        sit:  valor opcional , indicando se deve ou não adicionar a situação do aluno

    Returns:
        _type_: _dicionário com várias informações sobre a situação da turma._
    """
    
    r = f'Total de nota é {len(dados)}'
    r = f'A maior nota é {max(dados)}'
    r = f'A maior nota é {min(dados)}'
    
    média = sum(dados) / len(dados)
    r = f'A média nota é {média}'
    

          
   
    if média >= 7:
        r = f'A situação do aluno é APROVADO.'
    elif média <= 5:
        r = f'A situação do aluno é REPROVADO.'
    elif 5.1 <= média <= 6.9:
        r = f'A situação do aluno é RECUPERAÇÃO.'

    return r
    
    
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

