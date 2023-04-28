# 17- Programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

f = int(input('Informe um número e veja o seu fatorial calculado: '))
n = f
fat = f
var = 0
while n > 1:
    var = f - 1
    fat = fat * var
    f = var
    n = n - 1
print('O fatorial do número {} é: {}'.format(f, fat))

