#PEÇA AO USUARIO PARA DIGITAR ALGO E FILTRE O QUE FOR DIGITADO

a = (input('Digite algo'))
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?',a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?',a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta em maiusculo?',a.isupper())
print('Esta em minusculo?', a.islower())
print('Esta capitalizada?', a.istitle())