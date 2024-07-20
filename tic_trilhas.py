lista_produto = []
lista_unidade_de_medida = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]

def adiciona_produto():
    while True:
        try:
            nome_produto = input("Qual é o nome do produto? \n")
            unidade_de_medida_produto = int(input("Qual é a unidade de medida desejada? \n Escolha entre 1 e 7 (1.Quilograma, 2.Grama, 3.Litro, 4.Mililitro, 5.Unidade, 6.Metro, 7.Centímetro) \n"))
            for _ in range(len(lista_unidade_de_medida)):
                unidade_produto_escolhida = lista_unidade_de_medida[unidade_de_medida_produto - 1]
            quantidade_produto = int(input("Qual é a quantidade de produto? Por favor enserir valor numérico. \n"))
            descricao_produto = input("Qual é a descrição do produto? \n")
            id_produto = len(lista_produto) + 1 if len(lista_produto) != 0 else 1
            ultimo_valor = lista_produto[-1][0] if len(lista_produto) != 0 else 0
            if ultimo_valor > id_produto:
                id_produto = ultimo_valor
                id_produto+=1
            if nome_produto.lstrip() != ''  and descricao_produto.lstrip() != '':
                lista_produto.append([id_produto, nome_produto, unidade_produto_escolhida, quantidade_produto, descricao_produto])
                print("Produtos adicionado com sucesso!! :D \n")
                sair_ou_ficar = input("Deseja adicionar mais algum produto? Caso não queira digite 'N' \n")
                if sair_ou_ficar.upper() == "N":
                    print(f"Obrigado por adicionar um item a lista. \n itens da lista: {lista_produto} \n")
                    break
            else:
                print("Todos os campos devem ser preenchidos. \n")
        except Exception:
            print("Erro no cadastro do produto")

    return lista_produto

def remover_produto():
    while True:
        try:
            print(f"Itens em sua lista: \n {lista_produto} \n")
            id_produto = int(input("Deseja deletar algum produto? Escolha o ID do produto, por favor utilizar valor numérico.\n"))
            id_valido = 0 
            for i in range(len(lista_produto)):
                if lista_produto[i][0] == id_produto:
                    confirmar_remocao = input(f"Seria esse Item que gostaria de deletar? Se sim digite 'S': \n {lista_produto[i]} \n")
                    id_valido = id_produto
                    if confirmar_remocao.upper() == "S":
                        lista_produto.pop(i)
                        print(f"Valor escolhido deletado com sucesso!!\n Lista Atualizada {lista_produto}")
                        break
                    else:
                        break
            if id_valido == 0:
                print(f"ID do produto não localizado, por favor digitar um ID do produto existente. \n {lista_produto} \n")
            continuar_deletando = input("Deseja continuar deletando produto? Caso não queira, digite 'N' \n ")
            if continuar_deletando.upper() == "N":
                print(f"Obrigado!\n itens que restam {lista_produto}")
                break
        except Exception:
            print("Por favor digite um valor válido ou escolha um item existente.")

def pesquisa_produto():
    while True:
        try:
            pesquisa_produto = input("Por favor digite o nome do produto: \n ")
            nome_pesquisado = ''
            for i in range(len(lista_produto)):
                nome_produto = lista_produto[i][1]
                if pesquisa_produto in nome_produto:
                    nome_pesquisado = nome_produto
                    print(nome_pesquisado)
            if nome_pesquisado == '':
                print("Valor informado não foi encontrado.\n")
            sair_da_pesquisa = input("Deseja continuar pesquisando produtos? Para sair digite 'N' \n")
            if sair_da_pesquisa.upper() == 'N':
                print("Pesquisa encerrada! :D\n")
                break
        except Exception:
            print("Nome do produto inválido.")

print(""" 
╭━╮╭━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃┃╰╯┃┃╱╱╱╱╱╱╱╱╱╱╱╱┃┃
┃╭╮╭╮┣━━┳━┳━━┳━━┳━╯┣━━╮
┃┃┃┃┃┃┃━┫╭┫╭━┫╭╮┃╭╮┃╭╮┃
┃┃┃┃┃┃┃━┫┃┃╰━┫╭╮┃╰╯┃╰╯┃
╰╯╰╯╰┻━━┻╯╰━━┻╯╰┻━━┻━━╯
╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮
╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮
╭━━┳┫╰━┳━━┳━┳━╮╭━┻╮╭╋┳━━┳━━╮
┃╭━╋┫╭╮┃┃━┫╭┫╭╮┫┃━┫┃┣┫╭━┫╭╮┃
┃╰━┫┃╰╯┃┃━┫┃┃┃┃┃┃━┫╰┫┃╰━┫╰╯┃
╰━━┻┻━━┻━━┻╯╰╯╰┻━━┻━┻┻━━┻━━╯ \n""")


while True:
    try:
        print(f"Menu de Opção:\n 1.Adicionar produto \n 2.Remover produto \n 3.Pesquisar produtos \n 4.Sair do programa \n Lista de produto: \n{lista_produto} \n")
        op = int(input("Digite sua opção: "))
        if op == 1:
            adiciona_produto()
        elif op == 2:
            remover_produto()
        elif op == 3:
            pesquisa_produto()
        elif op == 4:
            print("Obrigado por participar da Listinha do mercado cibernético")
            break
        else:
            print("Por favor digite algum número entre 1 e 4")
        
    except Exception:
        print("valor inválido, por favor digite entre 1 e 4")