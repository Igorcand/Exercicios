#AVALIAÇÃO DE NUMEROS GERADO ALEATORIAMENTE

from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('OS valores sorteados foram : ', end= '')
for n in num:
    print(f'{n}', end= ' ')
print(f'\n O maior valor sorteado foi {max(num)}')
print(f' O menor valor sorteado foi {min(num)}')