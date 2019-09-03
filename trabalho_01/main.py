from grafo import Grafo
import time

g2 = Grafo()
for i in range(0,9):
    g2.new_no(i)

g2.nova_aresta(1,3,232)
g2.nova_aresta(1,2,32)
g2.nova_aresta(3,4,345)
g2.nova_aresta(2,4,324)
g2.nova_aresta(4,5,23)
g2.nova_aresta(5,6,23)
g2.nova_aresta(5,7,44)
g2.nova_aresta(6,7,23)
g2.nova_aresta(7,0,24)
g2.nova_aresta(0,4,24)
g2.nova_aresta(0,3,24)


g = Grafo()

for i in range(0,11):
    g.new_no(i)

g.nova_aresta(0,1,31)
g.nova_aresta(0,2,29)
g.nova_aresta(0,3,29)
g.nova_aresta(0,4,52)
g.nova_aresta(0,5,25)
g.nova_aresta(0,6,27)
g.nova_aresta(0,7,28)
g.nova_aresta(0,8,24)
g.nova_aresta(0,9,36)
g.nova_aresta(0,10,30)


g.nova_aresta(1,2,18)
g.nova_aresta(1,3,22)
g.nova_aresta(1,4,25)
g.nova_aresta(1,5,20)
g.nova_aresta(1,6,24)
g.nova_aresta(1,7,14)
g.nova_aresta(1,8,16)
g.nova_aresta(1,9,29)
g.nova_aresta(1,10,3)

g.nova_aresta(2,3,12)
g.nova_aresta(2,4,38)
g.nova_aresta(2,5,22)
g.nova_aresta(2,6,10)
g.nova_aresta(2,7,9)
g.nova_aresta(2,8,9)
g.nova_aresta(2,9,20)
g.nova_aresta(2,10,5)

g.nova_aresta(3,4,40)
g.nova_aresta(3,5,21)
g.nova_aresta(3,6,16)
g.nova_aresta(3,7,23)
g.nova_aresta(3,8,16)
g.nova_aresta(3,9,20)
g.nova_aresta(3,10,19)

g.nova_aresta(4,5,48)
g.nova_aresta(4,6,51)
g.nova_aresta(4,7,39)
g.nova_aresta(4,8,42)
g.nova_aresta(4,9,60)
g.nova_aresta(4,10,36)

g.nova_aresta(5,6,18)
g.nova_aresta(5,7,16)
g.nova_aresta(5,8,12)
g.nova_aresta(5,9,28)
g.nova_aresta(5,10,22)

g.nova_aresta(6,7,14)
g.nova_aresta(6,8,15)
g.nova_aresta(6,9,20)
g.nova_aresta(6,10,21)

g.nova_aresta(7,8,2)
g.nova_aresta(7,9,23)
g.nova_aresta(7,10,19)

g.nova_aresta(8,9,28)
g.nova_aresta(8,10,18)

g.nova_aresta(9,10,36)

print ("\nPressione 1 para ver o grafo com 6 nos e 11 arestas\n")
print ("\nou 2 para para ver o grafo com 11 nos e 55 arestas.\n")

n = 0

cidades ={ 0 : "Gama",
            1 : "Ceilandia",
            2 : "Taguatinga",
            3 : "Guara",
            4 : "Aguas Lindas",
            5 : "Riacho Fundo",
            6 : "Aguas Claras",
            7 : "P SUl",
            8 : "Samanbaia",
            9 : "Brasilia",
            10 : "M Norte"}

while(n is not 1 or n is not 2):
    n = input()
    if n is 1:
        print("Deseja ver o DFS ou Dijkstra")
        print("1 Para DFS")
        print("2 Para Dijkstra")
        print("3 Para comparar os dois metodos")
        m = 0
        while(m is not 1 or m is not 2 or m is not 3):
            m = input()
            if m is 1:
                g2.DFS(1)
                break
            if m is 2:
                g2.Dijkstra(1)
                break
            if m is 3:
                inicio = time.time()
                g2.DFS(1)
                fim = time.time()
                inicio1 = time.time()
                g2.Dijkstra(1)
                fim1 = time.time()
                print("O tempo necessario para realizar o DFS:")
                print(fim - inicio)                
                print("O tempo necessario para realizar o Dijstra:")
                print(fim1 - inicio1)
                break

    if n is 2:
        print("Escolha sua cidade de partida ou verifique a cidade que melhor lhe convem:")
        for i in range(0,11):
            lista = []
            lista.append(i)
            lista.append(cidades[i])
            print lista
        p = 15
        while True:
            p = input()
            if (p<0 or p>11):
                print("O codigo da cidade e invalido, por favor digite um codigo entre 0 e 10.")
            if p>=0 or p<=10:
                print("Esses sao os melhores caminhos para chegar as cidades que possuimos na nossa base de dados.")
                print( "Partindo de %s" % cidades[p])
                g.Dijkstra(p)
                break

    if n is 1 or n is 2:
        break
