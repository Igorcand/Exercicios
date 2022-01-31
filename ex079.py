#ADICIONANDO VALORES EM UM ARRAY

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado')
    r = str(input('Quer continuar? [S/N] ')).upper()[0]
    if r == 'N':
        break
print('=-' * 30)
lista.sort()
print(f'Voce adiciionou os valores {lista}')
print(f'Voce adicoinou {len(lista)} itens a sua lista')
lista.sort(reverse=True)
print(f'A lista em ordem decressente é {lista}')
print(f'O valor 5 está na lista? {lista.find(5)}')

