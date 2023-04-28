#1-  Ler 2 números do usuário para que seja impresso o maior deles.
# a = int(input('Informe o 1o número: '))
# b = int(input('informe o 2o número: '))
# if a > b:
#     print('O maior número digitado é {}.'.format(a))
# else:
#     print('O maior número digitado é {}.'.format(b))


# 2- Ler um valor e mostrar na tela se ele é positivo ou negativo:
# val = float(input('Informe um número positivo ou negativo:'))
# if val > 0:
#     print("Número positivo.")
# elif val < 0:
#     print("Número negativo.")
# else:
#     print("Numeral zero.")

#
# # 3- Verificar se uma letra digitada é F ou M , escrevendo M=masculino F=feminino, ou sexo inválido.
# letra = str(input("Informe a inicial do sexo:"))
# if letra == "F" or letra == "f":
#     print('Sexo feminino.')
# elif letra == "M" or letra == "m":
#     print('Sexo masculino.')
# else:
#     print('Sexo indefinido')


# # 4-  Programa que identifique se uma letra digitada é vogal ou consoante.
# letra = str(input('Informe uma letra para saber se é vogal ou consoante.'))
# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#     print("Vogal.")
# else:
#     print("Consoante.")
#
# print("Obrigado por participar.")


# 6- Programa que lê 3 números e mostra o maior deles.

n1 = int(input('Informe o 1o número: '))
n2 = int(input('Informe o 2o número: '))
n3 = int(input('Informe o 3o número: '))
maior = 0
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print('O maior número informado é {}.'.format(maior))


# 7-