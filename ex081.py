#DIGITANDO VALORES NAS RESPECTIVAS POSIÇÕES

lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('VALOR ADICIONADO...')
    r = str(input('Quer continuar? [S/N]')).upper()[0]
    if r in 'Nn':
        break
print(f'Voce digitou os valores : {lista}')
print(f'Voce adicionou {len(lista)} itens a sua lista')
lista.sort(reverse=True)
print(f'A lista em ordem decressente é {lista}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado')


