lista_produtos = []
lista_quantidade = []

def adicionar_produto():
    nome_produto = input("Digite o nome do produto: ")
    lista_produtos.append(nome_produto)
    quant_prod = int(input("Digite a quantidade dos produtos: "))
    lista_quantidade.append(quant_prod)

def mostrar_produto():
    for p in lista_produtos:
        print("Produto:", p)
    
    for q in lista_quantidade:
        print("Quantidade:", q)


def remover_produto():
    
    nome_produto = input("Digite o nome do produto: ")
    quant_prod = int(input("Digite a quantidade dos produtos: "))
    indice_prod = lista_produtos.index(nome_produto)
    indice_quant = lista_quantidade.index(quant_prod)
    del lista_produtos[indice_prod]
    del lista_quantidade[indice_quant]

    
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
            mostrar_produto()
            continue
        elif menu == 4:
            print("FINALIZANDO...")
            break



main()