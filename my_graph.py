# Name: Michal Golovanevsky
import sys

class Vertex:
    """represents each vertex in the graph"""
    def __init__(self,key):
        self.id = key
        self.connectedTo = []
        self.color = 'gray'

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    #Vertex Vertex =>
    def addNeighbor(self, nbr):
        #eliminates repeats
        if nbr not in self.connectedTo:
            #adds neighbor to the list
            self.connectedTo.append(nbr)
            nbr.addNeighbor(self)

    #Vertex => str
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    #Vertex => list
    def getConnections(self):
        return self.connectedTo

    #Vertex => int
    def getId(self):
        return self.id


class MyGraph:
    """contains a dictionary that maps vertex names to vertex objects"""
    def __init__(self, filename):
        """ reads in the specification of a graph and creates a graph using an adjacency list representation"""
        self.vertList = {}
        self.numVertices = 0
        self.build_graph(filename)
        self.twoColorable = True

    def print_graph(self):
         for key in self.vertList.keys():
             print(self.getVertex(key))

    def addVertex(self, key):
        if self.getVertex(key) is None:
            self.numVertices += 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex
        return self.getVertex(key)


    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None


    def __contains__(self, n):
        return n in self.vertList


    def addEdge(self, f, t):
        #checks the vertex is not already in the list
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        #connects the vertices to each other
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])


    def getVertices(self):
        return self.vertList.keys()


    def __iter__(self):
        return iter(self.vertList.values())


    #returns the length of a list of lists that shows which components are connected
    def conn_components(self):
        #calls helper function
        return len(self.dfs())


    #opens the file and builds the graph
    def build_graph(self, filename):
        num_vert = 0
        num_edges = 0
        try:
            #opens the file
            with open(filename, 'r', encoding='utf-8') as file:
                # loops line by line
                for line in file:
                    # line 1 is the number of vertices
                      pair = line.split()
                      self.addEdge(int(pair[0]), int(pair[1]))
        # if file doesn't exist
        except IOError:
            return 'file does not exists'


    def dfs(self):
        connectedComps = []
        #loops through the vertices
        for aVertex in self.vertList:
            vert = self.vertList[aVertex]
            #checks that a vertex is white
            if vert.getColor() == 'gray':
                connectedComp = [vert.id]
                #calls helper function
                self.dfsvisit(vert, connectedComp, 'white')
                #adds to list
                connectedComps.append(connectedComp)
        return connectedComps

    def oppositeColor(self, color):
        if color == 'white':
            return 'black'
        else:
            return 'white'


    def dfsvisit(self, startVertex, connectedComp, color):
        #visited vertices turn gray
        startVertex.setColor(color)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'gray':
                connectedComp.append(nextVertex.id)
                self.dfsvisit(nextVertex, connectedComp, self.oppositeColor(color))
            elif nextVertex.getColor() == color:
                self.twoColorable = False

def main(argv):
    g = MyGraph(argv[1])
    g.dfsvisit()
    if g.twoColorable:
        print('Is two-colorable')
    if not g.twoColorable:
        print('Is not two-colorable')
    print(g.conn_components() + ' connected component(s)')

if __name__ == '__main__':
    main(sys.argv)
