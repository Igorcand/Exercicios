#SABER A SOMA SOMA DE NUMEROS DIGITADOS

n = cont = soma = 0
while True:
    n = int(input('Digite um número[ 999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Voce digitou {cont} números e a soma deles foi de {soma}')