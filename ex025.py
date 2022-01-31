#VERIFIQUE SE EXISTE A PALAVRA SANTO NO NOME DIGITADO PELO USUARIO

nome =str(input('Qual é o seu nome?')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))