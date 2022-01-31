#MENU PARA DESCONTO DE ACORDO COM A FORMA DE PAGAMENTO

print('Loja de conveniencias')
print('==='*20)
valor = int(input('Preço das compras : R$'))
print('''FORMAS DE PAGAMENTO 
[ 1 ] A vista/ Cheque 
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Escolha sua opção: '))
if opçao == 1 :
    print('Seu produto sairá por {}'.format(valor - valor/10))
elif opçao == 2 :
    print('Seu produto sairá por {}'.format(valor - (valor*5)/100))
elif opçao == 3 :
    print('Seu produto sairá por {}'.format(valor))
elif opçao == 4 :
    print('Seu produto sairá por {}'.format(valor * 1.2))
else:
    print('Erro. tente novamente.')