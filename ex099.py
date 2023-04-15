
from time import sleep

def numero(* num):
    maior = cont = 0
    print('=-=' * 20)
    print('\nAnalisando os números.')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    
    
#Programa Principal
numero(1, 5, 6, 4, 8, 9)
numero(4, 5, 6)
numero(1, 6, 7, 9)
numero(1, 5)
numero()