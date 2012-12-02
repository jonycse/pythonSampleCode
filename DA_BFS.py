#DA_BFS.py

from collections import deque
class BFS:
    def __init__(self, node,edges, source):
        self.node = node
        self.edges = edges
        self.source = source
        self.color=['W' for i in range(0,node)] # W for White
        self.graph =color=[[False for i in range(0,node)] for j in range(0,node)]
        self.queue = deque()
        self.parent =[-1 for u in range(0,node)]

        # Start BFS algorithm
        self.construct_graph()
        self.bfs_traversal()

    def construct_graph(self):
        for u,v in self.edges:
            self.graph[u][v], self.graph[v][u] = True, True

    def bfs_traversal(self):

        self.queue.append(self.source)
        self.color[self.source] = 'B' # B for Black

        while len(self.queue):
            u =  self.queue.popleft()
            for v in range(0,self.node):
                if self.graph[u][v] == True and self.color[v]=='W':
                    self.color[v]='B'
                    self.queue.append(v)
                    self.parent[v]=u

    def print_shortest_path(self, destination):
        if destination==self.source:
            print destination,
        elif self.parent[destination] == -1:
            print "No Path"
        else:
            self.print_shortest_path(self.parent[destination])
            print "-> ",destination,



node = 8 # 8 nodes from 0 to 7
edges =[(0,1),(0,3),(1,2),(1,5),(2,7),(3,4),(3,6),(4,5),(5,7)] # bi-directional edge
source = 0 # set fist node (0) as source

bfs = BFS(node,edges,source)
print bfs.parent
bfs.print_shortest_path(5) # shortest path from 0 to 5
print
bfs.print_shortest_path(7) # shortest path from 0 to 7
