#O LIMITE DE VELOCIDADE É 80KM/H E A MULTA É DE 1 REAL POR KM EXCEDIDO

v = float(input('Digite uma velocidade de uma carro em km/h : '))
d = (v-80)*7
if v>80:
    print('Seu carro foi multado no valor de {} reais'.format(d))
else:
    print('Que bom, seu carro estava dentro do limite de velocidade.')
