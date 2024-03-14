lista_de_produtos = {}

def adicionar_produto():
    nome_prod = input("Digite o nome do produto: ")
    quant_prod = int(input("Digite a quantidade do produto: "))
    lista_de_produtos.setdefault(nome_prod, quant_prod)

def mostrar_lista():
    print(lista_de_produtos)
    

def remover_produto():
    nome_prod = input("Digite o nome do produto: ")
    del lista_de_produtos[nome_prod]

def main():

    while True:

        print("MENU\n1-Adicionar produto\n2-Remover produto\n3-Mostrar lista\n4-Sair")
        menu=int(input("OPC:"))

        if menu == 1:
            adicionar_produto()
            continue
        elif menu == 2:
            remover_produto()
            continue
        elif menu == 3:
            mostrar_lista()
            continue
        elif menu == 4:
            print("FINALIZANDO...")
            break



main()