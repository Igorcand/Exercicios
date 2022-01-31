#DIGITANDO VALORES NAS RESPECTIVAS POSIÇÕES E ANALISANDO

num = list()
pares = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]')).upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 ==0:
        pares.append(v)
    else:
        impar.append(v)
print('-=' * 30)
print(f'A lista completa é: {num}')
print(f'A lista dos pares é: {pares}')
print(f'A lista dos immpares é: {impar}')