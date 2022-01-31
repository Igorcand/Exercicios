#VERIFIQUE SE O NUMERO É PAR OU IMPAR

n = int(input('Digite um número: '))
res = n % 2
if res == 0:
    print('Seu número é par.')
else:
    print('Seu número é impar.')