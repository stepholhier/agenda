def adicionar_contato(nome, email, telefone):
    dados = {"nome": nome, "email": email, "telefone": telefone, "completada": False}
    lista.append(dados)
    print(f"Informações do contato: Nome: {nome}, E-mail: {email}, Telefone: {telefone}")
    return print ("Contato adicionado com sucesso")


def visualizar_contato(lista):
    print("\nLista de Contatos: ")
    for indice, dados in enumerate(lista, start=1):
        status = "❤️" if dados["completada"] else " "
        contato = dados["nome"]
        print(f"{indice}. [{status}] {contato}")

#Adicionando editar contato
# def editar_contato(lista):

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
    
    elif escolha == "7":
        break

print("Agenda finalizada com sucesso")