#VERIFICANDO QUEM TEM O MENOR E O MAIOR PESO DAS PESSOAS CADASTRADAS

temp = list()
princ = list()
perg = ''
cont = 1
maior = menor = 0
maispeso = menospeso = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]

    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja cadastrar mais pessoas?[S/N]')).upper()[0]
    if resp == 'N':
        break
    cont += 1

print(princ)
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi de {maior} quilos. Peso de ',end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} quilos. Peso de ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')


