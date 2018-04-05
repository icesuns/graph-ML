import math
import time
import random
import networkx as nx
import matplotlib.pyplot as plt

#generate random graph using ER model
def ERGrapjh(maxNumEdges, p, numOfVertices, path):

    #create file with current time
    path = path + str(time.time())+".txt"

    with open(path, 'w+') as f:
        index_of_edge = []

        i = -1
        while i < maxNumEdges:
            # generate the random number in [0,1)
            theta = random.random()
            # skipping edges
            k = math.ceil(math.log(theta, 1 - p)) - 1
            if k < 0:
                k = 0
            i = i + k + 1

            # decode the index of edge
            x = math.floor(i / numOfVertices)
            y = i % numOfVertices

            # discard the self-loop
            if x == y:
                continue

            s = str(x) + " " + str(y)+"\n"
            index_of_edge.append(s)

        # write edges into file, and discard the last edge
        j = 0
        while j < len(index_of_edge) -1:
            f.write(index_of_edge[j])
            j = j + 1



#generat Power-Law graph
def powerLawGraph(numVertex, path):
    g = nx.generators.random_graphs.barabasi_albert_graph(numVertex, 6)
    edges = g.edges()

    #name the file as current time
    path = path + str(time.time())+".txt"

    # g1 = nx.DiGraph()
    with open(path, 'w+') as f:
        for edge in edges:
            p = random.uniform(0, 1)
            if p <= 0.5:
                e = (edge[0],edge[1])
                # g1.add_edge(*e)
                s = str(edge[0])+" "+str(edge[1])+"\n"
                f.write(s)
            else:
                e = (edge[1], edge[0])
                # g1.add_edge(*e)
                s = str(edge[1]) + " " + str(edge[0])+"\n"
                f.write(s)

    # nx.draw(g1)
    # plt.show()



if __name__ == "__main__":
    powerLawGraph(20, "/home/icesun/Desktop/")


