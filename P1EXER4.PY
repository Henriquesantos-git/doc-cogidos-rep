#Crie um dicionário com 5 produtos e seus respectivos preços.
#Exemplo: {"Arroz": 20.0, "Feijão": 8.5, "Leite": 5.0, ...}
#Mostre a lista de produtos ao usuário.
#Permita que o usuário escolha três produtos digitando seus nomes.
#Calcule o valor total da compra.
#Se o produto digitado não existir, mostre uma mensagem de erro.
print("Bem vindo ao mercadinho")

#aqui faz o dicionario
produtos = {"Arroz":20.0, "Feijão": 8.5, "Leite": 5.0, "Acucar": 3.0, "Sal": 4.50,}

print("Produtos disponíveis:")
for produto in produtos:
    print(produto, "-", produtos[produto])

#total começa em 0
total = 0

#pedindo 3 produtos
for i in range(3):
    escolha = input("Digite o nome de um produto: ")

    if escolha in produtos:
        total = total + produtos[escolha]
    else:
        print("Produto não encontrado!")

#mostrar total da compra
print("Valor total da compra:", total)






