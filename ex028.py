#JOGUE ADIVINHA COM A MAQUINA

from random import randint
from time import sleep
pc = randint(0, 5)
print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
jo = int(input('Em que numero eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if jo==pc:
    print('Parabens, voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e não no {}!'.format(pc, jo))