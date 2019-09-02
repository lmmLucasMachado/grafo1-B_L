from grafo import Grafo

g = Grafo()
for i in range(0,9):
    g.new_no(i)
'''

g.nova_aresta(0,1,4)
g.nova_aresta(0,4,2)
g.nova_aresta(1,2,1)
g.nova_aresta(1,3,0)
g.nova_aresta(2,3,3)
g.nova_aresta(3,4,8)
g.nova_aresta(4,1,2)


g.new_no(0)
g.new_no(1)
g.new_no(2)
'''
g.nova_aresta(1,3,4)
g.nova_aresta(1,2,4)
g.nova_aresta(3,4,4)
g.nova_aresta(2,4,4)
g.nova_aresta(4,5,4)
g.nova_aresta(5,6,4)
g.nova_aresta(5,7,4)
g.nova_aresta(6,7,4)
g.nova_aresta(7,8,4)

g.DFS(1)
'''

g.new_no("Ceilandia")
g.new_no("Taguatinga")
g.new_no("Guara")

g.nova_aresta("ceilandia","taguatinga",15)
g.nova_aresta("ceilandia","Guara",20)
g.nova_aresta("Guara","taguatinga",10)
'''
