#LISTA DE COMPRAS

print('=='* 10)
print('LISTA DE COMPRAS')
print('=='* 10)
soma = 0
contmais1000 = 0
menor = 0
cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço:R$ '))
    cont += 1
    soma += preço
    if preço > 1000:
        contmais1000 += 1
    if cont == 1: #or preço < menor:
        menor = preço
        barato = nome
    else:
        if preço < preço:
            menor = preço
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar suas compras? ')).strip().upper()[0]
    if tipo == 'N':
        break

print(f'Suas compras vão custar R${soma:.2f} ')
print(f'Na sua lista de compras tem {contmais1000} produtos com o valor maiores que R$1000,00.')
print(f'O produto mais barato foi {menor} com o preço de R${menor:.2f} ')

