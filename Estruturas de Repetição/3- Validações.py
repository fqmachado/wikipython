
3- Programa que leia e valide as seguintes info:
a) nome; maior que 3 caracteres.
b) idade: entre 0 e 150
c) Salário: maior que zero.
d) Sexo: 'f' ou 'm'
e) Estado civil: s, c, v, d

nome = str(input('informe seus dados pessoais.\nPrimeiro, seu nome:'))
idade = int(input('Idade: '))
salário = float(input('Salário: '))
sexo = str(input('Sexo: F ou M ? '))
ec = str(input('Estado Civil: s=solteiro; c=casado; v=viúvo; d=divorciado'))

tam = len(nome)
for tam > 3:
    print('Nome: {}'.format(nome))
else:
    print('Isso são só as iniciais. Informe o nome inteiro.')
# ## não foi finalizado porque não consegui validar o tamanho do nome ###  MONIORIA  <<<<<<<<<<<<<

