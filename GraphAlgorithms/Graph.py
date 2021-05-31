class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [None for i in range(V)]
        for v in range(V):
            self.adj[v] = []  # create new list at every vertex

    def addEdge(self, v, w):
        """
        v <-> w
        """
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
    
    def adjacent(self, v):
        """
        finds all vertices adjacent to vertex 'v'
        """
        return self.adj(v)

    def degree(self, v):
        return len(self.adjacent(v))

    def maxDegree(self, v):
        max_so_far = 0
        for v in range(self.V):
            if self.degree(v) > max_so_far:
                max_so_far = self.degree(v)
        return max_so_far

    def averageDegree(self, v):
        return 2.0 * self.V / self.E  # using multiply by 2, because we have parallel edges here
    
    def numberOfSelfLoops(self):
        count = 0
        for v in range(self.V):
            for w in self.adjacent(v):
                if ( v == w):
                    count += 1
        return count / 2  # using /2 because we are using parallel edges




