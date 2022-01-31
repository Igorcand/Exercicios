#ACHE O SENO, COSSENO E A TANGENDE DE UM ANGULO


import math
an = float(input('Digite o angulo que voce deseja'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print("O seno do angulo é  {:.2f} \n o cosseno é {:.2f} \n e a tagente é {:.2f} ".format(sen, cos, tg))