#CLASSIFICAÇÃO DO BRASILEIRÃO

times = ('Palmeiras', 'Santos', 'Flamengo', 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Corinthians', 'Ponte Preta', 'Grêmio', 'Chapecoense', 'São Paulo','Cruzeiro','Fluminense','Sport','Coritiba','Internacional','Figueirense','Santa Cruz', 'América-MG')
print(f'Os cinco primeiros colocados do Brasileirão 2016 foram : {times[:5]}')
print(f'Os clubes que foram rebaixados em 2016 foram:{times[-4:]} ')
print(f'Os clubes em ordem alfabetica são : {sorted(times)}')
print(f'A chapecoense ficou na posição {times.index("Chapecoense")+1}')