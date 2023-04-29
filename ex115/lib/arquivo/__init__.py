from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt siginifica leitura de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt+ seginifica escreva um arquico de texo e o sinal de + é adicionar
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
        try:
            a = open(nome, 'rt')
        except:
            print('Erro ao ler o arquivo!')
        else:
            cabeçalho('PESSOAS CADASTRADAS')
            print(a.read())


