#FUNÇÃO PARA CALCULAR O FATORIAL

def fatorial(n, mostra=False):
    f = 1
    for c in range(n, 0, -1):
        if mostra:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, mostra=True))