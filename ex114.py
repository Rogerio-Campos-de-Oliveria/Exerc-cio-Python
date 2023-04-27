'''Exercício Python 114: Crie um código em Python
que teste se o site pudim está acessível pelo
computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')