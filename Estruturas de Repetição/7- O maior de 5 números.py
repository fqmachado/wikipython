# 
# 7- Um programa que leia 5 números (positivos) e informe o maior deles.
# 
# >>> Consegui fazer, mas quero avançar. Então:
# <<<<<<  MONITORIA: Para trabalhar com valores negativos, como buscar o maior? >>>>>>>>>

c = 1
lista = []
maior = 0
while c <= 5:
    dado = int(input('Informe o {}º número: '.format(c)))
    c = c + 1
    lista.append(dado)
for valor in lista:
    if valor > maior:
        maior = valor
print(lista)
print('O maior valor da lista é {}. '.format(maior))

