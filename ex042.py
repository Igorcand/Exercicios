#VERIFICAÇÃO DE TRIANGULOS

l1 = float(input('Primeiro segmento:'))
l2 = float(input('Segundo segmento:'))
l3 = float(input('Terceiro segmento:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2  and l1 == l2 == l3:
    print('Os segmentos PODEM formar um triangulo e é um triangulo equilatero.')
elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 == l2 or l1 == l3 or l2 == l3:
    print('Os segmentos PODEM formar um triangulo e é um triangulo isoceles.')
elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 != l2 != l3 :
    print('Os segmentos PODEM formar um triangulo e é um triangulo escaleno.')
else:
    print('Os segmentos NÃO PODEM formar um triangulo.')