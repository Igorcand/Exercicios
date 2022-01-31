#MENU PARA OPERAÇÕES ENTRE DOIS NUMEROS

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print(''' ----- MENU -----
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA ''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        print('A soma entre os dois numeros é {}.'.format(n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre os dois números é {} '.format(n1*n2))
    elif opcao == 3:
        if n1 > n2:
             print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Não existe número maior, eles são iguais.')
    elif opcao == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    else:
        'Opção não identificada, tente novamente...'
print('Fim do programa! Volte sempre.')

