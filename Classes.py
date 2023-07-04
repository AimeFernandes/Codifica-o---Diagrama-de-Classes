class Revista:
    def __init__ (self, titulo, issn, periodicidade):
        self.titulo =  titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = [ ] #Vetor que liga a classe Revista e a classe Edicao
        

    def addNovaEdicao(self, edicao):
        num_artigos = edicao.contarNumeroDeArtigo()
        if (num_artigos>=10 and num_artigos <=15):
            self.edicoes.append(edicao)
            return f"A edição foi lançada com sucesso!"
        elif (num_artigos<10):
            return f"São necessários no mínimo 10 artigos para lançar uma nova edição."
        else:
            return f"Uma edição comporta no máximos 15 artigos."

    def exibirEdicoes(self):
        for edicao in self.edicoes:
            print(edicao.exibirEdicao())


class Edicao:
    def __init__ (self, numero, volume, data):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = [ ] #Vetor que liga a classe Edicao e a classe Artigo

    def addNovosArtigos (self,artigo):
        self.artigos.append(artigo)

    def exibirEdicao(self):
        return f"Edição: " + str(self.numero) + " ; " + "Volume: " + str(self.volume) + " ; " + "Data: " + str(self.data)

    def showArtigos(self):
        for artigo in self.artigos:
            print(artigo.exibirArtigo()) 

    def contarNumeroDeArtigo(self):
        return len(self.artigos)
    
    def delArtigo(self,titulo):
        for artigo in self.artigos:
            if artigo.titulo == titulo:
                self.artigos.remove(artigo)
    

class Artigo:
    def __init__ (self,titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibirArtigo(self):
        return f"Título: " + str(self.titulo) + " ; " + "Autor: " + str(self.autor)


