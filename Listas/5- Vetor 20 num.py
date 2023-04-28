# 5- Prog que leia 20 numeros int e armazene-os em um vetor. E armazene os pares num vetor PAR e os ímpares num IMPAR.
#    E imprima os 3 vetores.

c = 20
i = 1
list = []
even = []
odd = []
while c > 0:
    num = int(input('Informe o {}º número: '.format(i)))
    list.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    i = i + 1
    c = c - 1

print('The complete list typed is: {}.\n The list of even numbers is: {}.\n And the list of odd numbers is: {}.'.format(list, even, odd))

