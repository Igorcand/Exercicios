#JOGAR PAR OU IMPAR COM A MAQUINA

print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
from random import randint
v = 0
while True:
    valor = int(input('Digite um valor: '))
    computador = randint(0, 10)
    resp = valor + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {valor} e o computador {computador}. Total de {resp}', end=' ')
    print('DEU PAR' if resp % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if resp % 2 == 0 :
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if resp % 2 == 1 :
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER. Voce ganhou {v} vezes')
