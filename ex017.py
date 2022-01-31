#DESCUBRA O VALOR DA HIPOTENUSA

import math
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do cateto adjacente?'))
#h = math.sqrt(co**2+ca**2)
hi = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(hi))