#Questão – Controle de Vendas
# produto = const50 = 0 
# quantidade_de_produtos = int(input("Digite a quantidade de produtos vendidos: "))
# for i in range(quantidade_de_produtos+=1):

# Questão – Controle de Vendas

total_vendas = 0
quantidade_de_produtos = int(input("Digite a quantidade de produtos vendidos: "))

for i in range(quantidade_de_produtos):
    valor = float(input(f"Digite o valor do produto {i+1}: "))
    total_vendas += valor

print(f"Total vendido: R$ {total_vendas:.2f}")
