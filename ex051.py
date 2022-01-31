#FAZENDO UMA PROGRESSÃO ARITIMÉTICA

p = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da sua PA:'))
for c in range(p, p+(10*r), r):
    print(c, end= ' ')