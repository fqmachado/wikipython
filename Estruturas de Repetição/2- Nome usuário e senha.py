2- Ler nome de usuário e senha e recusar senha igual ao nome de usuário, mostrando uma msg de erro e voltando
a pedir as informaçoes.

nome = str(input('Nome de usuário: '))
senha = str(input('Senha: '))
while senha == nome:
    print("Senha inválida. Escolha uma senha diferente do nome.")
    nome = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
print('Obrigado por se cadastrar.')