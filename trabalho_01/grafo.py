
from no import No
from aresta import Aresta

class Grafo:

    def __init__(self):
        self.lista_vertices = []
        self.lista_arestas = []

    def new_no(self, id_nome):
        self.lista_vertices.append(No(id_nome))
   
    def busca_aresta(self, u, v):  # Metodo recebe dois objetos do tipo Vertice
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_vertice(self, identificador):  # Metodo recebe um int
        for i in self.lista_vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def nova_aresta(self, origem, destino, peso):
        origem_aux = self.busca_vertice(origem)
        #print(origem)        
        destino_aux = self.busca_vertice(destino)

        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("############  ERROR  ############")

    def esta_vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False

    def busca_aresta(self, u, v): # metodo recebe dois objetos do tipo vertice
        for w in self.lista_arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_no(self, id_nome):  # metodo recebe um int
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def busca_adjacente(self, u):  # metodo recebe um vertice
        for i in range(len(self.lista_arestas)):
            origem = self.lista_arestas[i].getOrigem()
            destino = self.lista_arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # para que nao retorne o mesmo vertice seguidas vezes
                return destino
            else:
                return None

    # dfs
    def DFS(self):
        for v in self.lista_Vertices:
            v.setVisitado(False)

        for v in self.lista_Vertices:
            if (v.getVisitado() == False):
                self.visita(v)

    def visita(self, u):
        print("Visitando o vertice: %s" % u.getId())
        u.setVisitado(True)
        self.tempo += 1
        u.setImput(self.tempo)
        v = self.busca_Adjacente(u)  # retorna apenas n visitado ou nulo
        while v is not None:
            v.predecessor.append(u.getId())
            self.visita(v)
            v = self.busca_Adjacente(u)

        self.tempo += 1
        u.setOutput(self.tempo)
        print("Voltando para: ", u.predecessor)

    def estima(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())  # guarda apenas o id

    def Dijkstra(self, origem):
        fonte = self.busca_vertice(origem)
        if fonte is None:
            return "Vertce Nulo"

        self.inicializa_Fonte(fonte)
        lista = []
        resposta = []  # conjunto resposta
        for i in self.lista_Vertices:
            lista.append(i)
        while len(lista) != 0:
            lista.sort()  # ordeno a lista baseado na estimativa
            u = lista[0]
            v = self.busca_Adjacente(u)
            if v is None:
                for i in self.lista_Vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vertice visitara
                    i.setVisitado(
                        False)  # esse vertice entao preciso marcar como nao visitado pra bucar os adj de outro vertice
                self.tempo += 1
                resposta.append(lista[0])
                lista.pop(0)  # retiro vertice sem adjacente da lista

            else:
                w = self.busca_Aresta(u, v)
                if w is not None:
                    self.estima(u, v, w)

        print("Estimativas: ")
        for i in resposta:
            print(i)  # imprimo as respostas

    def imprime_grafo(self, origem, destino):
        if origem == destino:
            print("Fim")
        else:
            destino_Aux = self.busca_vertice(destino)
            
            print(destino_Aux.predecessor)

            if len(destino_Aux.predecessor) == 0:
                print("Nao ha caminho")
            else:
                print(destino_Aux.predecessor[0])
                self.imprime_Grafo(origem, destino_Aux.predecessor[0])
