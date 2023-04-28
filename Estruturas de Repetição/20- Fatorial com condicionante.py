# 20 - Alterar o programa do Fatorial (ex.17) , permitindo ao usuário calcular o fatorial várias vezes
#      e limitando o fatorial a números inteiros positivos e MENORES que 16.

f = int(input('Informe um número e veja o seu fatorial calculado: '))
n = f
fat = f
var = 0
if f >= 16:
    print('Apenas fatorial de números menores que 16. Fim do programa')
    exit()
else:
    while n > 1:
        var = f - 1
        fat = fat * var
        f = var
        n = n - 1
print('O fatorial do número {} é: {}'.format(f, fat))

# MONITORIA:  Como fazê-lo calcular várias vezes ???