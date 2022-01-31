#SE A DISTANCIA FOR MAIOR QUE 200KMO PREÇO POR KM É 0.5 SE FOR MAIOR É 0.45

d = float(input('Qual a distancia da sua viagem,em quilometros.?'))
if d<=200:
    print('O preço da sua passagem será de {:.1f} reais.'.format(d/0.5))
else:
    print('O preço da sua passagem será de {:.1f} reais.'.format(d/0.45))