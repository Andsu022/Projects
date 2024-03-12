class Aluno():
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self._media = None

    def media_aluno(self, n1, n2, n3):
        self._media = ((n1+n2+n3)/3)


    def exibir_aluno(self):
        print("Nome:",self._nome)
        print("Matrícula:",self._matricula)
        print("Media: %.2f"%(self._media))
        print("---------------------------------")

    @property
    def nome(self):
        return self._nome
    
    @property
    def matricula(self):
        return self._matricula
    
    @property
    def media(self):
        return self._media
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @media.setter
    def media(self, media):
        self._media = media
    

class Disciplina():
    def __init__(self):
        super().__init__()
        self._lista_alunos = []
        self._lista_alunos_final = {}

    def adicionar_aluno(self, aluno):
        self._lista_alunos.append(aluno)

    def remover_aluno(self, matr):
        for i in self._lista_alunos:
            if i.matricula == matr:
                self._lista_alunos.remove(i.matricula)
                self._lista_alunos.remove(i.nome)
                self._lista_alunos.remove(i.media)


    def exibir_lista(self):

        print("Lista total de alunos da disciplina:")
        for a in self._lista_alunos:
            print("Aluno:",a.nome)
            print("Matricula:",a.matricula)
            print("Média: %.2f"%(a.media))
            print("-----------------------")

    def lista_prova_final(self):

        for i in self._lista_alunos:
            if i.media < 7.0:
                md = i.media
                i.media = "{:.2f}".format(md)
                self._lista_alunos_final[i.nome] = i.media

        if len(self._lista_alunos_final)==0:
            print("Não há alunos de prova final !")
        else:
            print("Lista de alunos em prova final:")
            for chave, valor in self._lista_alunos_final.items():
                print(f"{chave}: {valor}")
                print("-----------------------")
            


def main():
    while True:

        menu = int(input("MENU\n1- Adicionar aluno\n2- Adicionar disciplina\n3- Ver lista de alunos total\n4- Adicionar aluno\n5- Remover aluno\n6- Encerrar disciplina\n7- Sair\nOPC: "))
        
        if menu == 7:
            print("ENCERRANDO ...")
            break

        elif menu == 1:
            nome = input("Digite o nome do aluno: ")
            matricula = int(input("Digite a matrícula: "))
            n1 = float(input("Digite a primeira nota: "))
            n2 = float(input("Digite a segunda nota: "))
            n3 = float(input("Digite a terceira nota: "))
            aluno = Aluno(nome, matricula)
            aluno.media_aluno(n1, n2, n3)

        elif menu == 2:
            nome_d = input("Nome da disciplina: ")
            d = Disciplina(nome_d)
        
        elif menu == 3:
            nome_d = input("Nome da disciplina: ")
            d.exibir_lista(nome_d)




main()
'''
nome = "Anderson"
matricula = 54321
n1 = 7.5
n2 = 9.6
n3 = 8.8

aluno = Aluno(nome, matricula)
aluno.media_aluno(n1, n2, n3)
aluno.exibir_aluno()
poo = Disciplina()
poo.adicionar_aluno(aluno)
poo.exibir_listas()
'''