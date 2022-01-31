#PEÇA AO USUARIO PARA DIGITAR DOIS NUMEROS E MOSTRE AS OPERAÇÕES BASICAS COM ESSES NUMEROS

n1 = int(input('Digite um numero'))
n2 = int(input("Digite outro"))
s = n1+n2
d = n1/n2
m = n1*n2
e = n1**n2
di = n1//n2
print('A soma é {},a divisão é {:.2}, a multiplicação é {}'.format(s,d,m), end='')
print('A divisão inteira é {}, e a \n potencia é {}'.format(di,e))
