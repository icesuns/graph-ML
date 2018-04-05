import numpy as np
import os


class Graph:
    def __init__(self, num_vertex):
        self.damping = 0.85
        self.esp = 0.0000001
        self.num_vertex = num_vertex
        self.outDegree = np.ones(shape=[self.num_vertex], dtype=int)
        self.adjMatrix = np.zeros(shape=[self.num_vertex, self.num_vertex], dtype=float)


    # construct adjacent matrix from file
    # edges are stored in files
    def getAdjMatrix(self, path):
        with open(path) as f:
            edges = f.readlines()
            for e in edges:
                indce = e.replace("\n", "").split(" ")
                x = int(indce[0])
                y = int(indce[1])
                self.adjMatrix[x][y] = 1
        # return  self.adjMatrix
        # print(self.adjMatrix)



    def getOutDegree(self):
        v1 = np.ones(shape=[self.num_vertex], dtype=int)
        self.outDegree = np.dot(self.adjMatrix, v1.T)
        # print(self.outDegree)
        # return self.outDegree


    def getPageRank(self):
        outDegree = self.outDegree
        pagerank = np.ones(shape=[self.num_vertex], dtype=float)

        # initialize the pagerank as 1/num_vertex
        for i in range(self.num_vertex):
            pagerank[i] = float(1.0 / self.num_vertex)
        # print(pagerank)

        personalization = np.multiply(1.0 / self.num_vertex, np.ones(shape=[self.num_vertex], dtype=float))
        probability = np.zeros(shape=[self.num_vertex, self.num_vertex], dtype=float)
        for i in range(self.num_vertex):
            if self.outDegree[i] == 0:
                outDegree[i] = 1
                for j in range(self.num_vertex):
                    probability[i][j] = float(1 / self.num_vertex)
            else:
                for j in range(self.num_vertex):
                    probability[i][j] = float(self.adjMatrix[i][j] / outDegree[i])
        # print(probability)
        # print("___________________")
        # print(probability.T)
        # print(probability.T)

        #iteration
        j = 0
        prePagerank = np.zeros(shape=[self.num_vertex], dtype=float)
        # print(prePagerank)
        while np.sum(np.abs(prePagerank - pagerank)) > self.esp:
            j = j + 1
            print("iteration", j)
            prePagerank = pagerank

            # print(prePagerank)
            pagerank = (np.multiply(self.damping, np.dot(probability.T, prePagerank.T))
                        + np.multiply((1 - self.damping), personalization.T)).T
            # print(pagerank)
        return pagerank











if __name__ == "__main__":
    dir = "/home/icesun/workspace/graph/"
    for index, path in enumerate(os.listdir(dir)):
        file = dir + "/" + path
        if(index > 0):
            break
        p = Graph(28)
        p.getAdjMatrix(file)
        print("------------------")
        p.getOutDegree()
        print("------------------")
        # print(p.outDegree)

        # print("------------------")
        #
        page = p.getPageRank()
        # print(page)

        a =0
        # print(len(page))
        for i in range(len(page)):
            # print(i)
            a = a + page[i]

        print(a)

