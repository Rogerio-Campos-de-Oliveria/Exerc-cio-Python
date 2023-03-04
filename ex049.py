'''Exercício Python 49: Refaça o DESAFIO 9, 
mostrando a tabuada de um número que o usuário 
escolher, só que agora utilizando um laço for.'''

while True:
    n = int(input('Digite a tabuada que você deseja: '))
    for c in range(0, 11):
        print(f'{n} x {c:2} = {n*c:2}')
    print()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('Até a Próxima!!!')
