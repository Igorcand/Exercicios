#TENTAR ADIVINHAR O NUMERO DO COMPUTADOR

from random import randint
from time import sleep

computador = randint(1, 10)
cont = 2
print('Vou pensar em um  número entre 1 e 10. Tente adivinhar!')
v = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
while not v == computador:
    v = int(input('Voce errou, tente de novo...'))
    print('PROCESSANDO...')
    sleep(1)
    if v != computador:
        cont += 1
print('O computador pensou em {} \n E o jogador tentou {} vezes. '.format(computador, cont))
