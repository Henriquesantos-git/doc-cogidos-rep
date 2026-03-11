#Peça ao usuário que digite uma lista de nomes separados por vírgula.
#Transforme essa entrada em uma lista.
#Sorteie um nome como vencedor e exiba na tela.
#Sorteie também três nomes diferentes como suplentes.
#Se o usuário digitar menos de 4 nomes, mostre uma mensagem de erro e peça novamente.

from random import choice

#aqui o programa guarda os nomes
nomes = []
print("Por favor, insira 10 nomes:")

#aqui o programa recolhe 10 nomes
for _ in range(10):
    nome = input("Digite dez nomes: ")
    nomes.append(nome)

#aqui o programa sortea o nome 
nome_sorteado = choice(nomes)
print(f"\nO nome sorteado é: {nome_sorteado}")









