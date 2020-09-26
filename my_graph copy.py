# Name: Michal Golovanevsky
# Section: 7
# Lab 9

class Vertex:
    """represents each vertex in the graph"""
    def __init__(self,key):
        # key each vertex holds
        self.id = key
        # list of connected vertices
        self.connectedTo = []
        #color of nodes
        self.color = 'white'

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
        # dictionary represents list of virtices
        self.vertList = {}
        # int represents how many vertices are in the graph
        self.numVertices = 0
        #calls helper function to open the file
        self.build_graph(filename)

    def print_graph(self):
         for key in self.vertList.keys():
             print(self.getVertex(key))

    #MyGraph int => Vertex
    #adds vertex to the graph
    def addVertex(self, key):
        if self.getVertex(key) is None:
            #increases number of vertices
            self.numVertices += 1
            #creates the new vertex
            newVertex = Vertex(key)
            #adds it to the list
            self.vertList[key] = newVertex
            return newVertex
        return self.getVertex(key)

    #MyGraph int => Vertex or None
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        #if vertex is not in the graph
        else:
            return None

    #MyGraph => boolean
    #n is vertex id
    def __contains__(self, n):
        return n in self.vertList

    #MyGraph id id =>
    #f and t are vertex ids
    #adds an edge between vertices
    def addEdge(self, f, t):
        #checks the vertex is not already in the list
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        #connects the vertices to each other
        self.vertList[f].addNeighbor(self.vertList[t])
        self.vertList[t].addNeighbor(self.vertList[f])

    #MyGraph => keys
    def getVertices(self):
        return self.vertList.keys()

    #MyGraph => values
    def __iter__(self):
        return iter(self.vertList.values())

    #MyGraph => list of lists
    #returns a list of lists that shows which components are connected
    def conn_components(self):
        #calls helper function
        return self.dfs()

    #MyGraph file =>
    #opens the file and builds the graph
    def build_graph(self, filename):
        num_vert = 0
        num_edges = 0
        try:
            # opens the file
            with open(filename, 'r', encoding='utf-8') as file:
                i = 0
                # loops line by line
                for line in file:
                    # line 1 is the number of vertices
                    if i == 0:
                        num_vert = int(line.split()[0])
                        for j in range(num_vert):
                            self.addVertex(j+1)
                    # line 2 is the number of edges
                    elif i == 1:
                        num_edges = int(line.split()[0])
                    else:
                        pair = line.split()
                        self.addEdge(int(pair[0]), int(pair[1]))
                    i += 1
        # if file doesn't exist
        except IOError:
            return 'file does not exists'

    #MyGraph => list
    #depth first search
    def dfs(self):
        connectedComps = []
        #loops through the vertices
        for aVertex in self.vertList:
            vert = self.vertList[aVertex]
            #checks that a vertex is white
            if vert.getColor() == 'white':
                connectedComp = [vert.id]
                #calls helper function
                self.dfsvisit(vert, connectedComp)
                #adds to list
                connectedComps.append(connectedComp)
        return connectedComps

    #MyGraph Vertex list =>
    #Marks vertecies as visited
    def dfsvisit(self, startVertex, connectedComp):
        #visited vertices turn gray
        startVertex.setColor('gray')
        #loops through adjacent vertices
        for nextVertex in startVertex.getConnections():
            #checks if adjacent is white
            if nextVertex.getColor() == 'white':
                #adds to the list
                connectedComp.append(nextVertex.id)
                self.dfsvisit(nextVertex, connectedComp)
        #sets to black after no more neighbors
        startVertex.setColor('black')
