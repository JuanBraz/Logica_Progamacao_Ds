usuarios = {}

while True:
    print()
    print(30*'_', 'Menu', 30*'_')
    print('1. Adicionar usuário.')
    print('2. Listar usuário.')
    print('3. Excluir usuario.')
    print('4. Sair.')
    print(66*'_')
    print()
    opcao = input('Digite a opção desejada: ')
    
    #Cadastrar
    
    if opcao == '1':
        nome = input('Digite um nome: ').upper()
        email = input('Digite um email: ').upper()
        senha = input('Digite uma senha: ').upper()  
        usuarios[nome] = {'nome' : nome, 'email' : email, 'senha' : senha}
        print(f'Usuário {nome} cadastrado com sucesso!')
    
    #Listar usuário    
     
    elif opcao == '2':
        if usuarios:
            print('\n--- Lista de Usuarios Cadastrados ---')
            for email , dados in usuarios.items():
                print(f'Nome: {dados['nome']}, Senha: {dados['senha']}, Email: {dados['email']}')
        else:
            print('Nenhum usuário encontrado!')
    
    #Excluir usuário
    
    elif opcao == '3':
        nome_remove = input('Digite o nome que deseja remover: ')
        if nome_remove in usuarios:
            del usuarios[nome_remove]
            print('Usuário removido com sucesso!')
        else:
            print('Usuário não econtrado')
            
    #Saída    
    
    elif opcao == '4':
        print('Saindo do Sistema!')
        break
    else:
        print('Digite uma opcao válida: ')