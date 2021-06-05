import igraph as ig

def plota_grafo(G):
    # apenas as cores usadas na coloração do grafo
    qtd_cores = len(set(G.vs["color"]))
    
    # define a paleta de cores
    palette = ig.RainbowPalette(n=qtd_cores)
    cores = [palette.get(i) for i in range(qtd_cores)]

    # cada vértice recebe uma cor do modelo RGBA
    for vertice in G.vs:
        vertice["color"] = cores[vertice["color"]]

    layout = G.layout("kk")
    ig.plot(G, layout=layout, bbox=(800, 800))

# arquivo contém a cor que cada vértice recebeu
def escreve_arquivo(G):
    file = open("resultado.txt", 'w')
   
    for vertice in G.vs:
        file.write(f'{vertice["color"]}\n')
    
    file.close()

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
    file = "grafos\petersen.txt"
    G = ig.Graph.Read_Adjacency(file).as_undirected()
    
    # lista de cores (representadas por inteiros)
    qtd_vertices = G.vcount()
    cores = [i for i in range(qtd_vertices)]

    # primeiramente os vértices não tem cores
    G.vs["color"] = None

    # label de cada vértice
    G.vs["label"] = cores

    coloracao_vertices(G,cores)
    escreve_arquivo(G)
    plota_grafo(G)

main()