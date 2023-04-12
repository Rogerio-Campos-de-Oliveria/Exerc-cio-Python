'''Exercício Python 093: Crie um programa que gerencie 
o aproveitamento de um jogador de futebol. O programa 
vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada 
partida. No final, tudo isso será guardado em um 
dicionário, incluindo o total de gols feitos durante o 
campeonato.'''

dados = dict()
partidas = list()
dados['nome'] = str(input('Qual é o nome do jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(0, tot):
     partidas.append (int(input(f'Quantos gols ele fez na {c+1}º partida? ')))
     
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)

print('=-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-=' * 20)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    → Na partida {i+1}, fez {v} gols. ')
print(f'Foi um total de {dados["total"]} gols.')
