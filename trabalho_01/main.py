from grafo import Grafo

g = Grafo()
'''
for i in range(0,5):
    g.new_no(i)

g.nova_aresta(0,1,4)
g.nova_aresta(0,4,2)
g.nova_aresta(1,2,1)
g.nova_aresta(1,3,0)
g.nova_aresta(2,3,3)
g.nova_aresta(3,4,8)
g.nova_aresta(4,1,2)
'''

g.new_no(0)
g.new_no(1)
g.new_no(2)

g.nova_aresta(0,1,4)
g.nova_aresta(1,2,4)
g.nova_aresta(2,0,4)

g.imprime_grafo(0,2)