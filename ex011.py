#ACHE A ÁREA E DESCUBRA QUANTAS LATAS DE TINTA PRECISA PARA PINTAR SABENDO QUE UMA LATA PINTA METADE DA ÁREA

a = float(input('Digite uma altura'))
l = float(input('Digite uma largura'))
area = a*l
tinta = area/2
print('Uma area de {} metros quadrados ira preciar de {} latas de tinta para ser pintada'.format(area,tinta))