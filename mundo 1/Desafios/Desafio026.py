print('procura letras a em uma frase qualquer...')
frase = str(input('Escreva teu nome : ')).strip().lower()
print(frase)
print('A frase tem um total de \33[32m{}\33[m letras a'.format(frase.count('a')))
print('A primeira letra a esta na posição \33[32m{}\33[m'.format(frase.find('a')+1))
print('A ultima vez que a letra a aparece na frase é na posição \33[32m{}\33[m'.format(frase.rfind('a')+1))