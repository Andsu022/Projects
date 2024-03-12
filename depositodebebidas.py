import abc
lista_produtos = {}
lista_clientes = {}
lista_func = {}

class Funcionario(abc.ABC):

    def __init__(self, nome_funcionario, matricula, senha):
        self._nome_funcionario = nome_funcionario
        self._matricula = matricula
        self._senha = senha


    @property
    def nome_funcionario(self):
        return self._nome_funcionario

    @property
    def matricula(self):
        return self._matricula
    
    @property
    def senha(self):
        return self._senha
    
    @nome_funcionario.setter
    def nome_funcionario(self, nome_funcionario):
        self._nome_funcionario = nome_funcionario

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @senha.setter
    def senha(self, senha):
        self._senha = senha


    @abc.abstractmethod
    def autenticarFuncionario(self):
        pass




class Atendente(Funcionario):

    def __init__(self, nome_funcionario, matricula, senha):
        super().__init__(nome_funcionario, matricula, senha)
        lista_func[matricula] = (nome_funcionario)


    def autenticarFuncionario(self, senha):
        if(senha == self._senha):
            return True
        else:
            return False
        
    def exibirfunc(self):
        print(lista_func)


class Gerente(Funcionario):
    def __init__(self, nome_funcionario, matricula, senha):
        super().__init__(nome_funcionario, matricula, senha)
        lista_func[matricula] = (nome_funcionario)

    def autenticarFuncionario(self, senha):
        if(senha == self._senha):
            return True
        else:
            return False
        
    def exibirfunc(self):
        print(lista_func)


class Cliente():

    def __init__(self, nome, cpf, endereco, id):
        self._nome_cliente = nome
        self._cpf = cpf
        self._endereco = endereco
        self._id_cliente = id
        lista_clientes[self._id_cliente] = (self._nome_cliente, self._cpf, self._endereco)

    @property
    def nome_cliente(self):
        return self._nome_cliente
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def id_cliente(self):
        return self._id_cliente
    
    @nome_cliente.setter
    def nome_cliente(self, nome):
        self._nome_cliente = nome
    
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @id_cliente.setter
    def id_cliente(self, id):
        self._id_cliente = id



    def exibirCliente(self):
        print(lista_clientes)



class Produto():
    
    def __init__(self, prod, preco, volume, id_prod, estoque):
        self._prod = prod
        self._preco = preco
        self._volume = volume
        self._id_prod = id_prod
        self._estoque = estoque
        lista_produtos[self._id_prod] = (self._prod, self._preco, self._volume, self._estoque)
        

    @property
    def prod(self):
        return self._prod
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def id_prod(self):
        return self._id_prod
    
    @property
    def volume(self):
        return self._volume
    
    @property
    def estoque(self):
        return self._estoque
    
    @prod.setter
    def prod(self, prod):
        self._prod = prod
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @volume.setter
    def volume(self, volume):
        self._volume = volume
    
    @estoque.setter
    def estoque(self, estoque):
        self._estoque = estoque

    @id_prod.setter
    def id_prod(self, id):
        self._id_prod = id


    def exibirProduto(self):
        print("Produto:", self._prod)
        print("Preço: R$ %.2f"%(self._preco))
        print("Volume:",self._volume)
        print("Quantidade em estoque:",self._estoque)
        print("ID do produto:",self._id_prod)
        print("----------------------------------------------------")
    

    def alterarEstoque(self, quantidade):
        self._estoque =- quantidade


class Venda():

    def __init__(self, prodt, cliente, atendente, quantidade):
        pass

    
    def efetuarVenda(self, prodt, cliente, atendente, quantidade):
        self._prodvenda = super().prodt.prod
        self._cliente_venda = cliente
        self._atendentenome = atendente
        self._quant_venda = quantidade
        self._valor = super().prodt.valor*quantidade
        super().prodt.estoque(quantidade)

    def exibirVenda(self):
        print("Produto:",self._prodvenda)
        print("Cliente:",self._cliente_venda)
        print("Vendedor:",self._atendentenome)
        print("Quantidade:",self._quant_venda)
        print("Valor:R$ %.2f"%(self._valor))


gerente  = Gerente("Anderson Luz", 200216, 9756)
atendente = Atendente("Andre Luz", 202402, 2556)
def main():
    print("--Login--\n")
    login = int(input("Digite a senha: "))
    if (gerente.autenticarFuncionario(login) == True) or (atendente.autenticarFuncionario(login) == True):
        
        while True:
            print("|Menu\n|1-Cadastrar cliente\n|2-Cadastrar produto\n|3-Cadastrar funcionário(acesso apenas do gerente)\n|4-Realizar venda\n|5-Exibir cliente\n|6-Exibir produto\n|7-Sair\n")
            menu = int(input("|Digite a opção desejada: "))
            
            if (menu == 7):
                print("ENCERRANDO SISTEMA...")
                break
            elif(menu == 1):
                cod_cliente = input("Digite um código identificador do cliente: ")
                nome = input("Digite o nome do cliente: ")
                cpf = int(input("Digite o cpf: "))
                endereco = input("Digite o endereço(apenas a rua e o numero): ")
                id = cod_cliente
                cod_cliente = Cliente(nome, cpf, endereco, id)
                lista_clientes[cod_cliente] = nome
                continue
            elif(menu == 2):
                cod_p = input("Digite um código identificador do produto: ")
                prod = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                volume = input("Digite o volume do produto(ex. 1L, 300ml): ")
                id_prod = cod_p
                estoque = int(input("Digite a quantidade em estoque: "))
                cod_p = Produto(prod, preco, volume, id_prod, estoque)
                lista_produtos[cod_p] = prod
                continue
            elif(menu == 3):
                    senha_gerente = int(input("Digite a senha: "))
                    if gerente.autenticarFuncionario(senha_gerente) == True:
                        nome_func = input("Digite o nome do funcionário: ")
                        matricula = input("Digite uma matrícula: ")
                        senha = int(input("Digite uma senha: "))
                        func = Atendente(nome_func, matricula, senha)
                        lista_func[matricula] = nome_func
                        continue
                    else:
                        print("ACESSO NEGADO !")
                        break
            elif(menu == 4):
                p = input("Digite o nome do produto: ")
                cliente =  input("Digite o nome do cliente: ")
                quant = input("Digite a quantidade do pedido: ")
                func = input("Digite o nome do atendente: ")
                v = Venda()
                v.efetuarVenda(p, cliente, func, quant)
                opc = int(input("Ver dados de venda: 1-Sim\n2-Não\nR:"))
                if opc == 1:
                    v.exibirVenda()
                else:
                    continue
            elif(menu == 5):
                cod_cliente.exibirCliente()
                continue
            elif(menu == 6):
                cod_p.exibirProduto()
                continue
            elif(menu == 7):
                print("Finalizando sistema...")
                break
    else:
        print("ACESSO NEGADO !")



main()