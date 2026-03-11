#1 Peça ao usuário para cadastrar um nome de usuário e uma senha.
#2 Depois, solicite que ele faça o login digitando novamente os dados.
#3 O programa deve verificar se o login está correto:

#aqui o programa recolhe o login e senha que o usuario escolheu
usuariocadastro = input("cadastre seu nome: ")
criarsenha  = float(input("crie sua senha: "))

#aqui ele coloca o nome e senha cadastrado
login = input("Digite seu nome")
Senha = float(input("Digite sua senha"))

#aqui o programa verifica se o login e senha esta certo se esta certo = login realizado com sucesso
if usuariocadastro == login and Senha == criarsenha:
    print("login realizado c om sucesso")

#aqui o programa ve se o login esta certo e a 
#senha diferente da cadastrada, se nao estiver igual a cadastrada = senha incorreta
elif usuariocadastro == login and Senha != criarsenha:
    print("Senha incorreta") 

#aqui o programa verifica se o usuario ta de acordo com o cadastrado se nao = usuario incorreto
elif usuariocadastro != login and Senha == criarsenha:
    print("Usuario incorreto")

#aqui o programa verifica se os dois estao errado = usuario e senha incorreto
else:
    print("Usuario e senha incorretos")
