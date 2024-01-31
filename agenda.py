def adicionar_contato(nome, email, telefone):
    dados = {"nome": nome, "email": email, "telefone": telefone, "completada": False}
    lista.append(dados)
    print(f"Informações do contato: Nome: {nome}, E-mail: {email}, Telefone: {telefone}")
    return print ("Contato adicionado com sucesso")


def visualizar_contato(lista):
    if not lista: 
        print("Não há contatos para exibir.")
        return
    print("\nLista de Contatos: ")
    for indice, contato in enumerate(lista, start=1):
        status = "❤️" if contato["completada"] else " " 
        nome = contato["nome"]
        email = contato["email"]
        telefone = contato["telefone"]
        print(f"{indice}. [{status}] Nome: {nome}, E-mail: {email}, Telefone: {telefone}")


def editar_contato(lista, indice_contato, novo_nome, novo_email, novo_telefone):
    indice_contato_atualizado = int(indice_contato) - 1
    if 0 <= indice_contato_atualizado < len(lista):
        contato_atualizado = lista[indice_contato_atualizado]
        contato_atualizado["nome"] = novo_nome
        contato_atualizado["email"] = novo_email
        contato_atualizado["telefone"] = novo_telefone
        print(f"Contato {indice_contato} foi atualizado com sucesso.")
    else:
        print("Índice de contato é inválido.")
    return

def contato_favorito(lista, indice_contato):
    indice_contato_atualizado = int(indice_contato) -1
    lista[indice_contato_atualizado] ["completada"] = True
    print(f"Contato{indice_contato} marcado como favorito")
    return 

def lista_favoritos(lista):
    if not lista: 
        print("Não há contatos favoritos.")
        return
    print("\nLista de Favoritos: ")
    for indice, contato in enumerate(lista, start=1):
        if contato["completada"]:  
            status = "❤️"
            nome = contato["nome"]
            email = contato["email"]
            telefone = contato["telefone"]
            print(f"{indice}. [{status}] Nome: {nome}, E-mail: {email}, Telefone: {telefone}")

def deletar_contato(lista, indice_contato):
    indice_contato_para_deletar = int(indice_contato) - 1
    if 0 <= indice_contato_para_deletar < len(lista):
        del lista[indice_contato_para_deletar]
        print(f"Contato {indice_contato} deletado com sucesso.")
    else:
        print("Índice de contato é inválido.")
    return

lista = []
while True:
    print("1. Adicionar contato: ")
    print("2. Visualizar contatos cadastrados: ")
    print("3. Editar contato: ")
    print("4. Adicionar contato aos favoritos: ")
    print("5. Ver lista de favoritos: ")
    print("6. Excluir contato: ")
    print("7. Sair")


    escolha = input("Digite sua escolha: ")
    
    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        email = input("Digite o seu e-mail: ")
        telefone = input("Digite seu número de telefone: ")
        adicionar_contato(nome, email, telefone)

    elif escolha == "2":
        visualizar_contato(lista)

    
    elif escolha == "3":
        visualizar_contato(lista)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_email = input("Digite o novo e-mail do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        editar_contato(lista, indice_contato, novo_nome, novo_email, novo_telefone)

    elif escolha == "4":
        visualizar_contato(lista)
        indice_contato = input("Digite o contato que deseja favoritar: ")
        contato_favorito(lista, indice_contato)
    

    elif escolha == "5":
        lista_favoritos(lista)


    elif escolha == "6":
        visualizar_contato(lista)
        indice_contato = input("Digite o número do contato que deseja excluir: ")
        deletar_contato(lista, indice_contato)
        visualizar_contato(lista)

    elif escolha == "7":
        break

print("Agenda finalizada com sucesso")