lista_produtos = []

while True:
    print()
    print(20*'*', 'Menu da Loja', 20*'*')
    print('1. Adicionar produto.')
    print('2. Atualizar quantidade de produto.')
    print('3. Listar todos os produtos.')
    print('4. Calcular o valor total do estoque.')
    print('5. Sair')
    print(66*'*')
    print()
    opcao = input('Digite a opção desejada: ')
    
    # Cadastro do produto:
    if opcao == '1':
        nome = input('Digite o produto que deseja cadastrar: ').upper()
        quant = int(input('Digite a quantidade do produto: '))
        valor = float(input('Digite o valor do produto: '))
         
        if nome != '':
            lista_produtos.append([nome, quant, valor])
            print(f'Produto {nome} cadastrado com sucesso!')
        else:
            print('Digite algum valor: ')
            
    # Atualizar a quantidade do produto 
    elif opcao == '2':
        nome  = input('Digite o nome do produto que deseja atualizar: ')
        nova_quant = int(input('Digite a nova quantidade: '))
        
        encontrado = False
        
        for produto in lista_produtos:
            if produto[0] == nome:
                produto[1] = nova_quant
                print(f'Quantidade do produto {nome} atualizada para {nova_quant}')
                encontrado = True
                break
        if not encontrado:
            print(f'O produto {nome} não foi encontrado!')      
            
    # Listagem dos produtos        
    elif opcao == '3':
        if len(lista_produtos) == 0:
            print('O inventario  está vazio!')
        else:
            print('Produtos no inventario:')
            for produto in lista_produtos:
                print(f'Nome: {produto[0]} | Quantidade: {produto[1]} | Valor: {produto[2]:.2f}')
            
    #Calcular o valor total em estoque
    elif opcao == '4':
        valor_total = 0
        for produto in lista_produtos:
            valor_total += lista_produtos[1] * produto[2]
        print(f'Valor total do inventario é: R${valor_total:.2f}')
    
    # Saida do sistema        
    elif opcao == '6':
        print('Saindo do Sistema!')
        break
    
    else:
        print('Digite uma opcao válida!')
    