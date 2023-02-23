from math import trunc
from math import sqrt
from random import choice
from random import shuffle
num = float(input('Digit um valor'))
print('O valor digitado foi {:.2f}'.format(trunc(num)))

cata = int(input('Digite o valor do cateto adjacente'))
cato = int(input('Digite o valor do cateto oposto'))
hipo = sqrt(cata**2+cato**2)
print('valor da hipo', hipo)

nome1 = str(input('Difite o nome 1'))
nome2 = str(input('Difite o nome 2'))
nome3 = str(input('Difite o nome 3'))
nome4 = str(input('Difite o nome 4'))
lista = [nome1, nome2, nome3, nome4]
print('O valor escolhido é o {}'.format(choice(lista)))
shuffle(lista)
print(lista)
