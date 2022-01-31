#UMA AVALIAÇÃO PARA A CATEGORIA DE ACORDO COM A IDADE

from datetime import date
nasc = int(input('Digite sua data de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Sua idade é {}.'.format(idade))
if idade <= 9:
    print('Sua categoria de natação seria: Mirim.')
elif 9 < idade <= 14:
    print('Sua categoria de natação seria: Infantil.')
elif 14 < idade <=19:
    print('Sua categoria de natação seria: Junior.')
elif idade == 20 :
    print('Sua categoria de natação seria: Senior.')
else:
    print('Sua categoria de natação seria: Master.')