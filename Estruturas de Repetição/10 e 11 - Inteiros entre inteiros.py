
# 10- Programa que receba 2 números inteiros e gere os num inteiros que estão no intervalo entre eles.
# 11- No memso programa, mostre a soma dos números ao final.

# <<<< MONITORIA: Não consegui, pois depende da ordem dos dois números. Só funciona de o primeiro for maior.

dado = int(input('Informe o 1º número inteiro (de 2).'))
dado2 = int(input('Informe o 2º número inteiro (de 2).'))
lista = []

if dado2 < dado:
    c = dado2 - dado
    while c > 1:
        lista.append(c)
        c = c -1
    else:
        c = dado - dado2
        while c > 1:
            lista.append(c)
            c = c -1
print('Lista de inteiros entre os 2 números informados: {}'.format lista[::-1])
soma = sum(lista)
print(soma)
