#TRATAR ERRO NO PYTHON

c = ('\033[m'     # sem cor
     '\033[0;30;41m' # vermelho
     )

def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('-' * tam)
    print(msg)
    print('-' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP ', 1)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)