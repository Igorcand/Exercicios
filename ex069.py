#CADASTRO DE PESSOAS 

conthomem = 0
contmulher20 = 0
contmais18 = 0
print('-=' * 20)
print('CADASTRO DE PESSOAS')
print('-=' * 20)
while True:
    nome = str(input('Digite o nome de alguem: '))
    idade = int(input('Digite a idade : '))
    if idade > 18:
        contmais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo dela [M/F] : ')).strip().upper()[0]
    if sexo == 'M':
        print('Dado salvo.')
        conthomem += 1
    elif sexo == 'F' and idade < 20:
        contmulher20 += 1
    else:
        print('Dado salvo')
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar o cadastro? [S/N] ')).strip().upper()[0]
    if tipo == 'S':
        print('OK, vamos continuar...')
    else:
        break
print('Cadastro finalizado')
print(f'Seu cadastro teve um total de {conthomem} homens')
print(f'Seu cadatro teve um total de {contmulher20} mulheres menores de 20 anos.')
print(f'Seu cadastro teve um total de {contmais18} pessoas maiores de 18 anos.')

