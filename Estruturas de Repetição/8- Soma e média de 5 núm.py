
# 8- Programa que leia 5 números e informe a soma e a média dos números.

# # <<<<< MONITORIA: Consegui fazer, mas está pythônico?

c = 1
lista = []
while c <= 5:
    dado = float(input('Informe o {}º número de 5: '.format(c)))
    c = c + 1
    lista.append(dado)
tam = len(lista)
soma = sum(lista)
med = soma / tam
print('A soma dos valores da lista é {:.2f} e a média deles é {:.2f} .'.format(soma, med))

