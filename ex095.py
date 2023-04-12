'''Exercício Python 095: Aprimore o desafio 93 para que 
ele funcione com vários jogadores, incluindo um sistema 
de visualização de detalhes do aproveitamento de cada 
jogador.'''

time = list()
dados = dict()
partidas = list()

#Lendo os dados
while True:
    print('=-=' * 20)
    dados.clear()
    dados['nome'] = str(input('Qual é o nome do jogador: '))
    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    partidas.clear()
    for c in range(0, tot):
        partidas.append (int(input(f'    Quantos gols ele fez na {c+1}º partida? ')))
        
    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
    time.append(dados.copy())
    
    
    print('=-=' * 20)
    resp = ' '
        
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
        if resp in 'SN':
            break
    if resp == 'N':
        break
    
#Mostrando os dados    
print('=-=' * 20)
print('  Cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()

print('=-=' * 20)
for  k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-=' * 20)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f'ERRO! Não existe jogado com código {busca}!')
    else:
        print(f'   -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('=-=' * 20)
print(' <<< VOLTE SEMPRE !!! >>> ')