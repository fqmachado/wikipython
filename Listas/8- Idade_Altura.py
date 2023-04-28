# 8- Prog que peça a idade e a altura de 5 pessoas, armazene cada info no seu respectivo vetor. Imprima a idade
#    e a altura na ordem inversa à ordem lida.

p = 2
a = 1
h = 1
alt = []
id = []

while p > 0:
    idade = int(input('Idade do {}º participante: '.format(a)))
    altura = float(input('Altura do {}º participante: '.format(h)))
    alt.append(altura)
    id.append(idade)
    p = p - 1
    a = a + 1
    h = h + 1
print('Lista das idades dos participantes: {}'.format(alt))
print('Lista das alturas dos participantes: {}'.format(id))
alt.reverse()
print(alt)
id.reverse()
print(id)


