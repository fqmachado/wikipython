# Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

c = 10
lista = []

while c > 0:
    num = int(input('Informe um número:'))
    lista.append(num)
    c = c - 1
print(lista[::-1])
