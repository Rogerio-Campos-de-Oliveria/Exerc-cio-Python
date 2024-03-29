'''Exercício Python 104: Crie um programa que tenha a 
função leiaInt(), que vai funcionar de forma semelhante 
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt
('Digite um n: ')'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('=-=' * 20)
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            print('=-=' * 20)
        if ok:
            break
    return f'Você acabou de digitar o número {valor}.'
 

#Programa Principal
n = leiaInt('Digite um número: ')
print('=-=' * 20)
print(n)
print('=-=' * 20)
