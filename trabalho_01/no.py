
class No():
    def __init__(self, id):
        self.id = id
        self.visitado = False
        self.predecessor = []

    def setVisitado(self, valor):
        self.visitado = valor

    def getVisitado(self):
        return self.visitado

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa
    
    def __str__(self):
        cidades ={ 0 : "Gama",
                   1 : "Ceilandia",
                   2 : "Taguatinga",
                   3 : "Guara",
                   4 : "Aguas Lindas",
                   5 : "Riacho Fundo I",
                   6 : "Riacho Fundo II",
                   7 : "P SUl",
                   8 : "Plano Piloto",
                   9 : "Brasilia",
                   10 : "Lago Sul",
                   11 : "Lago Norte",
                   12 : "M Norte"}
        return (" Vertice  : %s \n Estimativa: %i \n" % (cidades[self.id], self.estimativa))  # imprimir o predecesso

