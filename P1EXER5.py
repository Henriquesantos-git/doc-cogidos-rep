# Nosso catálogo de livros com quantidades
catalogo = {
    "Dom Casmurro": 3,
    "1984": 2,
    "O Senhor dos Anéis": 1
}

# Pergunta ao usuário qual livro ele quer
livro = input("Digite o nome do livro que deseja emprestar: ")

# Verifica se o livro existe no catálogo
if livro in catalogo:
    # Se existe, verifica se ainda tem unidades
    if catalogo[livro] > 0:
        catalogo[livro] = catalogo[livro] - 1  # tira 1 do estoque
        print("Empréstimo realizado com sucesso!")
    else:
        print("Este livro está indisponível no momento.")
else:
    print("Livro não encontrado no catálogo.")

# Mostra o catálogo atualizado
print("\nCatálogo atualizado:")
for titulo in catalogo:  # percorre cada chave do dicionário
    print(titulo, ":", catalogo[titulo], "unidades")