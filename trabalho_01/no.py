
class No():
    def __init__(self, id):
        self.id = id
        self.visitado = False
        self.predecessor = []
        self.estimativa = 999999

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
        return (" Vertice  : %s \n Estimativa: %i \n Tempo(%i\%i): " % (
            self.id, self.estimativa, self.input, self.output))  # imprimir o predecesso
