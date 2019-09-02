from grafo import Grafo

g = Grafo()
for i in range(0,9):
    g.new_no(i)

g.nova_aresta(1,3,232)
g.nova_aresta(1,2,32)
g.nova_aresta(3,4,345)
g.nova_aresta(2,4,324)
g.nova_aresta(4,5,23)
g.nova_aresta(5,6,23)
g.nova_aresta(5,7,44)
g.nova_aresta(6,7,23)
g.nova_aresta(7,11)

print("Aplicando DFS")
print("(busca em largura")

g.DFS(1)

g.Dijkstra(1)

'''

g.new_no("Ceilandia")
g.new_no("Taguatinga")
g.new_no("Guara")

g.nova_aresta("ceilandia","taguatinga",15)
g.nova_aresta("ceilandia","Guara",20)
g.nova_aresta("Guara","taguatinga",10)
'''
