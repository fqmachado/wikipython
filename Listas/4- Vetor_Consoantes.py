# 4- Prog que leia um vetor de 5 caracteres e diga quantas consoantes forma lidas. Imprima as consoantes.

i = 0
c = 5
lista = []
cons = 0
vogais = ["a", "e", "i", "o", "u"]
vog = 0

while c > 0:
    i += 1
    letra = str(input('Informe a {}ª letra: '.format(i)))
    if len(letra) > 1:
        print('Fim do programa. Recomece e digite somente 1 letra por vez.')
        exit()
    c = c - 1
    lista.append(letra)
    if letra in vogais:
        vog = vog + 1
    else:
        cons = cons + 1

print('A lista de letras impressas é {}, contendo {} vogais e {} consoantes. '.format(lista, vog, cons))

