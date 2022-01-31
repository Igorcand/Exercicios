#FUNÇÃO PARA DIGITAR UMA MENSAGEM ENTRE TRAÇOS

def escreva(mensagem):
    tam = len(mensagem) + 4
    print('-' * tam)
    print(f'  {mensagem}')
    print('-' * tam)



msg = str(input('Digite uma mensagem: '))
escreva(msg)