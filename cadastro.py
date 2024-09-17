lista_usuario = []

while True:
    print()
    print(30*'*', 'Menu', 30*'*')
    print('1. Cadastrar usuário.')
    print('2. Listar usuário.')
    print('3. Excluir usuario.')
    print('4. Buscar pelo nome.')
    print('5. Sair')
    print(66*'*')
    print()
    opcao = input('Digite a opção desejada: ')
    
    #Cadastrar usuário
    if opcao == '1':
        nome = input('Digite o nome que deseja cadastrar: ').upper()
        
        if nome != '':
            lista_usuario.append(nome)
            print(f'Usuário {nome} cadastrado com sucesso!')
        else:
            print('Digite algum valor: ')
            
    #Listar usuário     
    elif opcao == '2':
        for i, n in enumerate(lista_usuario):
            print(f'{i + 1}° {n}')

    #Excluir usuário
    elif opcao == '3':
        
        for i, n in enumerate(lista_usuario):
            print(f'{i}° {n}')
        
        posicao = int(input('Digite um numero do usuario que deseja excluir: '))
        
        for j, _ in enumerate(lista_usuario):
            if j == posicao:
                lista_usuario.pop(j)
                print(f'Usuário da posição {j} foi removido!')
                
        
        '''
        for i in lista_usuario:
            if nome == i:
                lista_usuario.remove(i)
                print('Usuario removido com sucesso')
        '''
    #Buscar pelo nome
    elif opcao == '4':
        nome_buscar = input('Digite o nome que deseje buscar na lista: ').upper
        for i in lista_usuario:
            if i == nome_buscar:
                print (i)
                
    #Saida do sistema    
    elif opcao == '5':
        print('Saindo do Sistema!')
        break
    else:
        print('Digite uma opcao válida: ')
        