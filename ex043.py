#VERIFICAÇÃO DO IMC

peso = float(input('Digite sua massa, em kg : '))
altura = float(input('Digite sua altura, em metros : '))
imc = peso/(altura)**2
if imc <=18.5 :
    print('Seu imc é de {:.2f} e sua categoria é : Abaixo do peso.'.format(imc))
elif 18.5 < imc <= 25 :
    print('Seu imc é de {:.2f} e sua categoria é : Peso ideal.'.format(imc))
elif 25 < imc <= 30 :
    print('Seu imc é de {:.2f} e sua categoria é : Sobrepeso.'.format(imc))
elif 30 < imc <= 40 :
    print('Seu imc é de {:.2f} e sua categoria é : Obesidade.'.format(imc))
else:
    print('Seu imc é de {:.2f} e sua categoria é : Obesidade mórbita.'.format(imc))