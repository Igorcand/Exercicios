#VERIFICAÇÃO DE ALISTAMENTO MILITAR

from datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade < 18:
    print('Voce ainda não se alistou para o serviço militar. Faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Já se passaram {} anos desde que voce se alistou para o serviço militar.'.format(idade - 18))
else:
    print('Está no ano que voce deve se alistar para o serviço militar')