
# 12- Programa gerador de tabuada. Gerar a tabuada de qq num inteiro de 1 a 10. O usuário deve informar
#     de qual número ele deseja ver a tabuada.

num = int(input('Escolha um número de 1 a 10 e obtenha sua tabuada: '))
c = 1
while c <= 10:
    tab = c * num
    print('{} x {} = {}'.format(c, num, tab))
    c = c + 1

