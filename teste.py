class Aluno():
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self._notas = []
        self._media = None
    
    def inserir_notas(self, n1, n2, n3):
        self._notas.append(n1)
        self._notas.append(n2)
        self._notas.append(n3)

        self._media = (n1+n2+n3)/3


    @property
    def nome(self):
        return self._nome
    
    @property
    def notas(self):
        return self._notas
    
    @property
    def matricula(self):
        return self._matricula
    
    @property
    def media(self):
        return self._media
    
    @media.setter
    def media(self, media):
        self._media = media


class Disciplina():

    def __init__(self):
        super().__init__()
        self.lista_alunos = {}
        self.lista_aprovados = []

    def inserir_aluno(self, aluno):
        md = aluno.media
        aluno.media = "{:.2f}".format(md)
        self.lista_alunos[aluno.matricula] = (aluno.nome, aluno.media)


    def mostrar_lista_alunos(self):
        print(self.lista_alunos)
    
    
    def alunos_aprovados(self):
        for a in self.lista_alunos:
            if a.media >= 7:
                self.lista_aprovados.append(a)



        for i in self.lista_aprovados:
            print('|Aluno Aprovado: %s\nMédia: %.2f' %(i.nome, i.media))
            print("|---------------------|")




def main():
    print("|MENU|\n|1-Adicionar aluno\n|2-Adicionar notas\n|3-Adicionar disciplina\n4-")






a1 = Aluno('Anderson', 12345)
a1.inserir_notas(8.0, 8.5, 9.8)
a2 = Aluno('Ana Clara', 54321)
a2.inserir_notas(8.5, 9.7, 8.2)
poo = Disciplina()
poo.inserir_aluno(a1)
poo.inserir_aluno(a2)
#poo.alunos_aprovados()
poo.mostrar_lista_alunos()