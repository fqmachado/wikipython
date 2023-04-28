
 # 6- programa que imprima na tela os números 1 a 20 um embaixo do outro, e depois, um ao laod do outro.

x = 1
while x <= 20:
    print(x)
    x = x + 1

for c in range(1,21):
    print(c, end = '')
    print(', ' if c < 20 else '.', end='')
print()

