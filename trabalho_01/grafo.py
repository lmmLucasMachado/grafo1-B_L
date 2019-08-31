#criação do grafo
#grafo direcionado
import no.py
import aresta.py

class Grafo:

    def __init__(self):
        self.lista_vertices = []
        self.lista_arestas = []

    def new_no():
        self.lista_vertices.append(No(id_nome))

    def nova_Aresta(self, origem, destino, peso):  # Método recebe dois identificadores
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))  # Aresta(u,v) e Aresta(v,u)

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

    # Depth first search
    def DFS(self):
        for v in self.lista_Vertices:
            v.setVisitado(False)

        for v in self.lista_Vertices:
            if (v.getVisitado() == False):
                self.visita(v)

    def visita(self, u):
        
        print("Visitando o no: %s" % u.getId())
        
        u.setVisitado(True)
        
        v = self.busca_adjacente(u)  # retorna apenas não visitado ou nulo
        
        while v is not None:
            v.predecessor.append(u.getId())
            self.visita(v)
            v = self.busca_Adjacente(u)

        print("Voltando para: ", u.predecessor)
    

    def estima(self, u, v, w):
        if v.getEstimativa() > (u.getEstimativa() + w.getPeso()):
            v.setEstimativa(u.getEstimativa() + w.getPeso())
            v.predecessor.append(u.getId())  # guarda apenas o id

    def Dijkstra(self, origem):
        fonte = self.busca_Vertice(origem)
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
                for i in self.lista_Vertices:  # como o vetice u marcou seus adj como visitado nenhum outro vértice visitara
                    i.setVisitado(
                        False)  # esse vertice então preciso marcar como não visitado pra bucar os adj de outro vertice
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


    '''
    def imprime_Grafo_com_Destino(self, origem, destino):
        destino_Aux = self.busca_Vertice(destino)
        if len(destino_Aux.predecessor) == 0:
            print("Não ha caminho")
        else:
            print(destino)
            self.imprime_Grafo(origem, destino)
    '''
