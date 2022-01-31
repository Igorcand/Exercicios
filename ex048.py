#A SOMA DE TODOS OS MULTIPLOS DE 3 ENTRE 3 E 500

cont = 0
soma = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))