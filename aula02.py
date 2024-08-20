# Tipos de concatenação
# Concatenação com sinal (+)
#num = int(input('Digite um número inteiro:'))

#não é possivel concatenar numero inteiro usando esse metodo, a menos que
# converta o numero inteiro em uma string
#print('Ola, ' + str(num) +' . Seja bem-vindo!')
#print(type(num))

#concatenação com a (,)
#print('O numero digitando é:',num)

# Concatenção com sstring(f)
#print(f'O numero digitando é: {num} usando a concatenação "f"')

#div = num / 3
# Usando format para formatação numérica
#limitando a quantidade de casas decimais
#print(f'O resultado da divisão é {div:.2f}')



# Função para receber as informações do usuário
nome = input("Digite o seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo!")
email = input("Digite o seu e-mail: ")
telefone = int(input("Digite o seu telefone: "))

# Função para calcular o gasto mensal com gasolina e álcool

# Distância diária e mensal
distancia_diaria = 64
distancia_diaria = 
distancia_mensal = 1280 

# preço combustível
preco_gasolina = 6.50
preco_alcool = 5.00

# Consumo de combustível
consumo_gasolina = 91,4
consumo_alcool = 106,6

# Cálculo do gasto mensal de combustível
gasto_gasolina = preco_gasolina * consumo_gasolina
gasto_alcool = preco_alcool * consumo_alcool

print(f"E-mail: {email}")
print(f"Telefone: {telefone}")
print(f"\nGasto mensal com gasolina: R${gasto_gasolina:.2f}")
print(f"Gasto mensal com álcool: R${gasto_alcool:.2f}")
print(f"Média de quilômetros rodados mensalmente: {distancia_mensal:.2f} km")
