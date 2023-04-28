# 1- Programa que leia um vetor de 5 números inteiros e mostre-os.

c = 5
lista = []
while c > 0:
    num = int(input('Informe um número:'))
    lista.append(num)
    c = c - 1
print(lista)