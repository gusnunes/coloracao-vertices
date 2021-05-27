import igraph as ig

def define_cor(cores, cores_vizinhos):
    for opcao in cores:
        if opcao not in cores_vizinhos:
            return opcao

def coloracao_vertices(G,cores):
    for vertice in G.vs:
        vizinhos = G.neighbors(vertice)
        cores_vizinhos = [G.vs[i]["color"] for i in vizinhos]
        
        cor_disponivel = define_cor(cores,cores_vizinhos)
        vertice["color"] = cor_disponivel

def main():
    # lê o grafo
    G = ig.Graph.Read_Adjacency("petersen.txt").as_undirected()
    qtd_vertices = G.vcount()

    # cores que serao usadas no grafo
    palette = ig.RainbowPalette(n=qtd_vertices)
    cores = [palette.get(i) for i in range(qtd_vertices)]
    
    # primeiramente os vértices não tem cores
    G.vs["color"] = None

    coloracao_vertices(G,cores)

    # "fruchterman_reingold"
    layout = G.layout("kk")
    ig.plot(G, layout=layout, bbox=(800, 800))

    #ig.plot(G)

main()