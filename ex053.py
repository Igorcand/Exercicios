#MOSTRANDO OS AMINOACIDOS CORRESPONDENTES

from textwrap import wrap

dic = {'UUU':'Phe', 'CUU':'Leu', 'UUA':'leu', 'AAG':'Lisina','UCU':'Ser','UAU':'Tyr', 'CAA':'Gln'}

rna = input('Digite o RNA: ')

rna = wrap(rna, 3)
cadeia = ''
n = 1
final = ''
for seq in rna:
    if seq not in dic.get(seq):
        cadeia += dic.get(seq) + '-'

for i in range(len(cadeia) - n):
    final = final + cadeia[i]

print(f'Cadeia de Aminoácidos: {final}')