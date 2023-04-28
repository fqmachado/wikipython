
# 13- Programa que peça 2 números (base e expoente), calcule e mostre o primeiro num elevado ao 2o num.
#     Não utilize a função potência da linguagem.

base = int(input('Informe a base: '))
exp = int(input('Informe o expoente: '))
pot = 0

if exp == 1:
    print("Resultado: {}.".format(base))
    elif base == 1:
    print("Resultado: 1")
    elif exp == 0:
    print("Resultado: 1")
else:
    while exp > 1:
    pot = base * base
    exp = exp - 1
print(pot)
