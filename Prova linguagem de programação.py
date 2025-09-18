from random import choice

nome = input("\nOlá, Seja bem vindo a biblioteca, digite seu nome: ") #aqui vai recolher o nome
idade= int(input("\nAgora digite sua idade: ")) #aqui vai recolher idade 

infantil12 = {  #aqui sao os livros de 12 anos
    "O Mundo de Sofia": 3,
    "O Caçador De Pipas": 2,
    "A Menina Que Roubava Livros": 1
}
adolescente17 ={ #aqui sao os livros de 12 a 17 anos
"Harry Potter": 3,
"A Rainha Vermelha": 2,
"Porque tanta pressa de crescer": 1
}
Maiores18 = { #aqui sao os livros para maiores de 18 anos
"Rangers ordem dos arqueiros": 3,
"Quincas borba - Machado de Assis": 2,
"Roube como um artista": 1
}
print(f"\n Os livros que temos são: \ncategoria: infantis {infantil12} \ncategoria juvenis 12 a 17 anos: {adolescente17} \ncategoria adultos +18 anos: {Maiores18}. ")
print(f"agora vamos sortear um livro que combine com sua categoria")

if idade <= 11: # if = se idade for menor que 11 vai aparecer o print
    print(f"\nInfelizmente voce nao pode ser sorteado para pegar livro.")
    #o print é oque voce vai escrever para o usario ler
elif idade == 12:# elif = se nao idade exatamente igual 12 mostra o print
    livro = choice(list(infantil12.keys()))#aqui vai sortear um livro da variavel infatil12
    print(f"\n{nome}, Voce pode pegar livros infantis, iremos sortear um para voce. ! {livro}")
    print(f"\nObrigado por usar a biblioteca, {nome}, volte sempre")
    print("\nBoa leitura do livro !")
     #o print é oque voce vai escrever para o usario ler
elif idade <17:# elif = se nao idade menor que 17 mostra o print
    livro = choice(list(adolescente17.keys()))#aqui vai sortear um livro da variavel adolescente17
    print(f"\n{nome}, Voce pode pegar livros juvenis, iremos sortear um para voce. ! {livro}")
    print(f"\nObrigado por usar a biblioteca, {nome}, volte sempre")
    print("\nBoa leitura do livro !")
     #o print é oque voce vai escrever para o usario ler
elif idade >= 18:# elif = se nao idade maior ou igual que 18 mostra o print
    todos_os_livros = {**Maiores18, **adolescente17, **infantil12}
    livro = choice(list(todos_os_livros.keys()))#aqui vai sortear um livro da variavel maiores18
    print(f"\n{nome}, como maior de idade voce tem direito a todas as categoria de livros da biblioteca")
    print(f"O livro sorteado foi: {livro}.")
    print(f"\nObrigado por usar a biblioteca, {nome}, volte sempre")
    print("\nBoa leitura do livro !")
    #o print é oque voce vai escrever para o usario ler
else:
    print("idade invalida")