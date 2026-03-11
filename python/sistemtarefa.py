# Gerenciador de Tarefas
tarefas = [] #armazenar as tarefas em uma lista

while True: #loop infinito para exibir o menu e processar as opções do usuário

    print("\nGerenciador de Tarefas") #exibe o menu de opções para o usuario
    print("1 - Adicionar tarefa") #opção para adicionar uma nova tarefa
    print("2 - Listar tarefas") #opção para listar todas as tarefas cadastradas
    print("3 - Concluir tarefa") #opção para marcar uma tarefa como concluída
    print("4 - Remover tarefa") #opção para remover uma tarefa da lista
    print("5 - Sair")#opção para sair do gerenciador de tarefas

    opcao = input("Escolha uma opção: ").strip() #lê a opção escolhida pelo usuário e remove espaços em branco extras
    print("Valor digitado:", opcao) #exibe o valor digitado pelo usuário para fins de depuração

    if opcao == "1":#opção para adicionar uma nova tarefa

        nome = input("Nome da tarefa: ")#lê o nome da tarefa a ser adicionada
        descricao = input("Descrição: ")#lê a descrição da tarefa a ser adicionada
        prioridade = input("Prioridade (baixa/media/alta): ")#lê a prioridade da tarefa a ser adicionada
        id_tarefas = len(tarefas) + 1 #gera um ID único para a tarefa com base no número de tarefas já cadastradas
        tarefa = {                    #dicionário para armazenar os detalhes da tarefa
            "id": id_tarefas,         #atribui o ID gerado à tarefa
            "nome": nome,             #atribui o nome da tarefa ao dicionário
            "descricao": descricao,   #atribui a descrição da tarefa ao dicionário
            "prioridade": prioridade, #atribui a prioridade da tarefa ao dicionário
            "status": "pendente"      #atribui o status inicial da tarefa como "pendente"
        }

        tarefas.append(tarefa)        #adiciona a tarefa ao final da lista de tarefas

        print(f"Tarefa '{nome}' adicionada com sucesso!") #exibe uma mensagem de confirmação indicando que a tarefa foi adicionada com sucesso

    elif opcao == "2":      #opção para listar todas as tarefas cadastradas 
        if len(tarefas) == 0:#verifica se a lista de tarefas está vazia
            print("nenhuma tarefa cadastrada.") #exibe uma mensagem indicando que não há tarefas cadastradas
        else: #se houver tarefas cadastradas, percorre a lista de tarefas e exibe os detalhes de cada tarefa
            for tarefa in tarefas:#percorre cada tarefa na lista de tarefas
                print("\n-----------")#exibe uma linha de separação entre as tarefas para melhor visualização
                print("ID", tarefa["id"]) #exibe o ID da tarefa
                print("Nome:", tarefa["nome"])#exibe o nome da tarefa
                print("Descrição:", tarefa["descricao"])#exibe a descrição da tarefa
                print("Prioridade:", tarefa["prioridade"])#exibe a prioridade da tarefa
                print("status:", tarefa["status"])#exibe o status da tarefa (pendente ou concluída)

    elif opcao == "3": #opção para marcar uma tarefa como concluída
        if len(tarefas) == 0: #verifica se a lista de tarefas está vazia
            print("Nenhuma tarefa para concluir.") #exibe uma mensagem indicando que não há tarefas para concluir
        else:#se houver tarefas cadastradas, exibe a lista de tarefas e solicita ao usuário o ID da tarefa que deseja concluir
            
            while True: #loop para permitir que o usuário conclua várias tarefas sem precisar voltar ao menu principal
               
                print("\nTarefas cadastradas: ")#exibe uma mensagem indicando que as tarefas cadastradas serão listadas a seguir
                
                for tarefa in tarefas: #percorre cada tarefa na lista de tarefas e exibe o ID, nome e status de cada tarefa para que o usuário possa identificar qual tarefa deseja concluir
                    print("ID", tarefa["id"], "-", tarefa["nome"], "-", tarefa["status"]) #exibe o ID, nome e status de cada tarefa para que o usuário possa identificar qual tarefa deseja concluir
                
                id_concluir = int(input("\nDigite o ID da tarefa que deseja concluir: "))#solicita ao usuário que digite o ID da tarefa que deseja marcar como concluída e converte a entrada para um número inteiro
                
                for tarefa in tarefas:#percorre cada tarefa na lista de tarefas para encontrar a tarefa com o ID correspondente ao ID digitado pelo usuário
                    if  tarefa["id"] == id_concluir:#verifica se o ID da tarefa atual é igual ao ID digitado pelo usuário
                        tarefa["status"] = "concluida" #se o ID da tarefa for igual ao ID digitado pelo usuário, atualiza o status da tarefa para "concluída"
                        print(f"tarefa concluida com sucesso!")   #exibe uma mensagem de confirmação indicando que a tarefa foi marcada como concluída com sucesso
                        break #interrompe o loop após encontrar a tarefa correspondente e marcar como concluída   
                continuar = input("\nDeseja concluir outra tarefa? (s/n): ").lower()#solicita ao usuário que informe se deseja concluir outra tarefa e converte a resposta para minúscula para facilitar a comparação
                if continuar == "n":#se o usuário digitar "n", interrompe o loop para concluir tarefas e retorna ao menu principal
                    break                                   
    elif opcao == "4":
        if len(tarefa)== 0:#verifica se a lista de tarefas está vazia
            print("Nenhuma tarefa para remover.")#exibe uma mensagem indicando que não há tarefas para remover
        else:#se houver tarefas cadastradas, exibe a lista de tarefas e solicita ao usuário o número da tarefa que deseja remover
            print("\nTarefas cadastradas: ")#exibe uma mensagem indicando que as tarefas cadastradas serão listadas a seguir

            for i, tarefa in enumerate(tarefas):#percorre cada tarefa na lista de tarefas usando a função enumerate para obter o índice e a tarefa em si, e exibe o número da tarefa (índice + 1), nome, descrição, prioridade e status de cada tarefa para que o usuário possa identificar qual tarefa deseja remover
                print(f"{i + 1} - Nome: {tarefa['nome']} | Descrição: {tarefa['descricao']} | Prioridade: {tarefa['prioridade']} | Status: {tarefa['status']}")#exibe o número da tarefa (índice + 1), nome, descrição, prioridade e status de cada tarefa para que o usuário possa identificar qual tarefa deseja remover
            numero = int(input("Digite o numero da tarefa que deseja remover: "))#solicita ao usuário que digite o número da tarefa que deseja remover e converte a entrada para um número inteiro
            if numero >= 1 and numero <= len(tarefas):#verifica se o número digitado pelo usuário é válido (entre 1 e o número total de tarefas)
                del tarefas[numero - 1]#remove a tarefa da lista de tarefas usando o número digitado pelo usuário (ajustado para o índice da lista, que começa em 0)
                print("Tarefa removida com sucesso!")#exibe uma mensagem de confirmação indicando que a tarefa foi removida com sucesso
            else:#se o número digitado pelo usuário for inválido (menor que 1 ou maior que o número total de tarefas), exibe uma mensagem de erro indicando que o número é inválido e solicita ao usuário que tente novamente
                print("Número inválido. Por favor, tente novamente.")#exibe uma mensagem de erro indicando que o número é inválido e solicita ao usuário que tente novamente

    elif opcao == "5":#opção para sair do gerenciador de tarefas
        print("\nSaindo do gerenciador de tarefas...")#exibe uma mensagem indicando que o usuário está saindo do gerenciador de tarefas
        break#interrompe o loop infinito para encerrar o programa

  
