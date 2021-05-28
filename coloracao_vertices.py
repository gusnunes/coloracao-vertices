import igraph as ig

def plota_grafo(G):
    layout = G.layout("kk")
    ig.plot(G, layout=layout, bbox=(800, 800))

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
    file = "petersen.txt"
    G = ig.Graph.Read_Adjacency(file).as_undirected()
    
    qtd_vertices = G.vcount()

    # cores que serao usadas no grafo
    palette = ig.RainbowPalette(n=qtd_vertices)
    cores = [palette.get(i) for i in range(qtd_vertices)]
    
    # primeiramente os vértices não tem cores
    G.vs["color"] = None

    coloracao_vertices(G,cores)

    plota_grafo(G)

main()