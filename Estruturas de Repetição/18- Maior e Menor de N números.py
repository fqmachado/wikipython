# 18- Dado um conjunto de N números, informe o maior valor, o menor valor e a soma deles.

# MONITORIA: dificuldade com exercícios de maior e menor.

lista = [1, 4, 52, 8, 7, 56, 45, 12, 31, 98]
tam = len(lista)
cont = 0
maior = 0
menor = 0
while cont > 0:
    var = lista.pop(0)
    
    if var > maior:
        maior = var
    elif var < menor:
        menor = var
    else:
        cont = cont + 1
print(maior)

