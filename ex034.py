#QUEM TIVER O SALARIO MAIOR QUE 1250 O AUMENTO SERÁ DE 10% E QUEM TIVER MENOS SERÁ DE 15%

s = float(input('Digite o seu salário: '))
if s>1250:
    print('Seu novo saláro será de {:.2f} reais. '.format(s*1.1))
else:
    print('Seu novo salario será de {:.2f} reais. '.format(s*1.15))