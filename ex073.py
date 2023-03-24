'''Exercício Python 73: Crie uma tupla preenchida com os 20 
primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times = ('Palmeiras','Flamengo', 
         'Internacional', 'Gremio', 'Sao Paulo', 
         'Atletico-MG', 'Athletico-PR', 
         'Cruzeiro', 'Botafogo', 'Santos', 
         'Bahia', 'Fluminense', 'Corinthians', 
         'Chapecoense', 'Ceara', 'Vasco da Gama', 
         'Sport Recife', 'America-MG', 
         'Vitoria', 'Parana' )


print('=-=' * 20)
print("{:^50}".format("RESULTADO BRASILEIRÃO/2018"))
print('=-=' * 20)
print(f'Os 5 primeiros times do Brasileirão/2018 fora {times[:5]}')
print('=-=' * 20)
print(f'Os quatros últimos times do brasileirão foram {times[-4:]}')
print('=-=' * 20)
print(f'Times em ordem alfabéticas: {sorted(times)}')
print('=-=' * 20)
print(f'A Chapecoense ficou na {times.index("Chapecoense")+1}ª poição.')
print('=-=' * 20)
