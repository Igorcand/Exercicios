#UM CONTADOR DE NUMEROS POR VEZ VERIFICANDO QUANTOS NUMEROS PARES FORAM INFORMADOS

cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor:'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce informou {} numeros PARES  e a soma foi de {}'.format(cont, soma))