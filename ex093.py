#FILTRANANDO ESTATISTICAS DE UM JOGADOR

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gol na partida {c + 1}: ')))
jogador['gols'] =partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'   => Na partida {k}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
