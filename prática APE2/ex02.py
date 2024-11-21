while True:
    senha = int(input('Senha: '))
    if senha == 2002:
        break
    elif senha != 2002:
        print('Senha inválida')
print('Acesso Permitido')