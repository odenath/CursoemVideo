n = int(input('Digite o número:'))
print('Analisando o {} seu antecessor é o {} e o sucessor é {}'.format(n, n-1, n+1))
n1 = int(input('Digite um valor'))
print('O seu dobro é {}, seu triplo é{} \n e a sua raiz quadrada é{:.3f}'.format(n1*2, n1*3, n1**(1/2)))

l1 = float(input('Nota 1:'))
l2 = float(input('Nota 2:'))
media = (l1+l2)/2
print('A média é {:.2f}'.format(media))

t1 = float(input('Escreva o tamanho em metros e eu devolvo em cm e mm'))
print('O tamanho de {} metros é {:.0f}cm  e {:.0f}mm'.format(t1, (t1*100), t1*1000))

real = float(input('Quanto dinheiro vc tem na carteira?'))
dolar = real / 3.25
print('Com {} você pode comprar {:.2f} dólares'.format(real, dolar))

largura = float(input('Digite a largura da parede em metros com .'))
altura = float(input('Digite a altura da parede em metros com .'))
area = largura*altura
pintura = area/2
print('A área da sua parede é {} m e vai gastar {}litros'.format(area, pintura))

sal = float(input('Digite o salario'))
print('O salário com ajuste fica {}reais'.format(sal*1.15))

km = float(input('Quantos km rodados?'))
dias = float(input('Quantos dias'))
total = (60*dias)+(0.15*km)
print('O valor total da corrida dado o fato que cada dia custa '
      '60 reais e 0,15 centavos por km rodado ficou em {}'.format(total))




