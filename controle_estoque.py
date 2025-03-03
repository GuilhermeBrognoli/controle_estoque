import time

produtos = []

def cadastro_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produto["preco"] = preco
            produto["quantidade"] = quantidade
            time.sleep(1)
            print("Processando...")
            time.sleep(4)
            print(f"O produto '{produto['nome']}' foi atualizado!")
            break

    else:
        novo_produto = {
            "Nome": nome,
            "Preco": preco,
            "Quantidade": quantidade
            }
        produtos.append(novo_produto)
        time.sleep(1)
        print("Processando...")
        time.sleep(4)
        print(f"O produto '{nome}' foi cadastrado com sucesso!")
        
def listar_produto():
    if not produtos:
        print("Não há produtos cadastrados!")
    else:
        for produto in produtos:
            print(f"Nome: {produto["nome"]}, Preço: {produto["preco"]}, Quantidade: {produto["quantidade"]}")     

def remover_produto():
    nome = input("Nome do produto a ser removido: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            time.sleep(1)
            print("Processando...")
            time.sleep(4)
            print(f"O produto '{produto['nome']}' foi removido!")
            break
    else:
        print("Produto não encontrado!")   

def atualizar_quantidade():
    nome = input("Nome do produto: ")
    quantidade = int(input("Nova quantidade: "))
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produto["quantidade"] = quantidade
            time.sleep(1)
            print("Processando...")
            time.sleep(4)
            print(f"A quantidade do produto '{produto['nome']}' foi atualizada!")
            break
    else:
        print("Produto não encontrado!")                    

def menu():
   
    while True:
        time.sleep(2)
        print("1 - Cadastro de produto")
        time.sleep(0.5)
        print("2 - Listar produtos cadastrados")
        time.sleep(0.5)
        print("3 - Remover produto")
        time.sleep(0.5)
        print("4 - Atualizar quantidade do produto")
        time.sleep(0.5)
        print("5 - Sair", '\n')
        time.sleep(1)
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            cadastro_produto()
            
        elif opcao == 2:
            time.sleep(2)
            print('\n')
            listar_produto()
            print('\n')

        elif opcao == 3:
            time.sleep(2)
            print('\n')
            remover_produto()
            print('\n')   

        elif opcao == 4:
            time.sleep(2)
            print('\n')
            atualizar_quantidade()
            print('\n')      
            
        elif opcao == 5:
            print("Saindo...")
            break

        else:
            print("Opção invalida!")
            time.sleep(2)
            print("Digite uma das opções abaixo:", '\n')
            time.sleep(2)


menu()



    