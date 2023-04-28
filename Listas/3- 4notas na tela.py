# 4- Prog que leia 4 notas e mostre as notas e sua média na tela.

c = 5
n = 0
lista = []

while c > 0:
    n = n + 1
    num = int(input('Informe a {}ªnota: '.format(n)))
    lista.append(num)
    c = c - 1
soma = sum(lista)
count = len(lista)
avr = soma / count
print('As notas são {}, e sua média é {}.'.format(lista, avr))

# MONITORIA: como mostrar a lista sem os colchetes ?