
# 9- Programa que imprima na tela apenas os números ímpares entre 1 e 50.

c = 0
par = []
impar = []
while c <= 50:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
    c = c + 1
print('Eis abaixo a lista dos números ímpares entre 1 e 50:')
print(impar)

