#FUNÇÃO PARA CALCULAR ÁREA

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a}m²')


print('Controle de terrenos')
print('--' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
