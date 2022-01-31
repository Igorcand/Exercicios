#FAÇA UM VALIDADOR DE EMPRESTIMO

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos voce pretende pagar? '))
prest = casa/(anos*12)
lim = (30/100)*salario
if prest <= lim :
    print('Seu empredtimo foi aprovado. Sua prestação será de {:.2f} por mes. '.format(prest))
else:
    print('Seu emprestimo está negado')