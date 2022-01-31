#VERIFICANDO O SEXO

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} salvo com sucesso'.format(sexo))
