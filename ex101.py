#FUNÇÃO PARA VERIFICAR SE UMA PESSOA PODE VOTAR OU NÃO

from datetime import date
def voto(v):
    if v < 16:
        print(f'Com {idade} anos: VOTO NEGADO.')
    elif 16 == v or v == 17:
        print(f'Com {idade} anos: VOTO OPICIONAL')
    elif  18 <= v <= 64:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: VOTO OPICIONAL')


nasc = int(input('Em qual ano você nasceu? ' ))
idade = date.today().year - nasc
voto(idade)