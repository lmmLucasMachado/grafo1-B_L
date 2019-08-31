#criação do grafo
#grafo direcionado
import no.py

class Grafo:

    def __init__(self):
        self.lista_vertices = []
        self.lista_arestas = []

    def new_no():
        self.lista_vertices.append(No(id_nome))

    def nova_Aresta(self, origem, destino):  # Método recebe dois identificadores
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("############### Erro ###############")
            print("Aresta invalida")

    def esta_vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False

    def busca_aresta(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_no(self, id_nome):  # Método recebe um int
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def busca_adjacente(self, u):  # Método recebe um vertice
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # Para que não retorn o mesmo vertice seguidas veses
                return destino
            else:
                return None
