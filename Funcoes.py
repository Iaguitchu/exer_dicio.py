def perguntar():
    return input("Oque deseja realizar?\n" +
           "<I> - Para Inserir um usuário\n" +
           "<P> - Para Pesquisar um usuário\n" +
           "<E> - Para Excluir um usuário\n" +
           "<L> - Para Listar um usuário\n" +
           "Opção desejada: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada?: ").upper()]

def pesquisar(dicionario):
    pesquisa = input("Digite o login para pesquisar: ").upper()
    if pesquisa in dicionario.keys():
        print(f"O usuário é {pesquisa} e seu nome é {dicionario[pesquisa][0]}")
    else:
        print("Não existe esse login!")



def excluir(dicionario):
    deletar = input("Digite um usuário para excluir: ").upper()
    if deletar in dicionario.keys():
        dicionario.pop(deletar)

    print(dicionario)

def listar(dicionario):
    decisao = "S"
    lista = []
    while decisao == "S":
        usuario = input("Digite os usuários: ").upper()
        if usuario in dicionario.keys():
            lista.append(usuario)
        elif usuario == {}:
            print("Dicionário está vazio!")
        elif usuario != dicionario.keys():
            print("Não está na lista")


        decisao = input("deseja continuar?s/n").upper()
        if decisao != "S" or "N":
            print("Você precisa digitar S para sim ou N para não")
            pass
            decisao = "S"


    print(lista)

'''
    deletar = input("Digite um usuário para excluir: ").upper()
    x = -1
    for i in dicionario.keys():
        if deletar == i:
             x = i
    if x == -1:
        print("Não existe")
    else:
        dicionario.pop(x)
    print(dicionario)
'''








