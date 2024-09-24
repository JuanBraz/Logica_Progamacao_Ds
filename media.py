alunos = {}
while True:
    print()
    print(30*'_', 'Menu', 30*'_')
    print('1. Adicionar alunos.')
    print('2. Listar alunos e suas médias.')
    print('3. Sair.')
    print(66*'_')
    print()
    opcao = input('Digite a opção desejada: ')
    
    #Cadastrar
    
    if opcao == '1':
        nome = input('Digite o nome do aluno: ')
        nota1 = int(input('Digite a primeira nota: '))
        nota2 = int(input('Digite a segunda nota: '))
        nota3 = int(input('Digite a terceira nota: '))
        soma = nota1 + nota2 + nota3 
        media = soma /3 
        alunos[nome] = {'nome' : nome, 'Nota 1' : nota1, 'Nota 2' : nota2, 'Nota 3' : nota3, 'media' : media}
        print(f'Aluno {nome} cadastrado com sucesso!')
        
    #Listar usuário    
     
    elif opcao == '2':
        if alunos:
            print('\n--- Lista de Alunos Cadastrados ---')
            for i , dados in alunos.items():
                print(f'Nome: {dados['nome']}, Media: {dados['media']:.2f}')
        else:
            print('Nenhum usuário encontrado!')
                
    #Saida do sistema
    
    elif opcao == '3':
        print('Saindo do Sistema!')
        break
    else:
        print('Digite uma opcao válida!')