
class DFS:
    def __init__(self, node,edges):
        self.node = node
        self.edges = edges
        self.color=['W' for i in range(0,node)] # W for White
        self.graph =color=[[False for i in range(0,node)] for j in range(0,node)]
        self.parent =[-1 for u in range(0,node)]

        # Start DFS
        self.construct_graph()
        self.dfs_traversal()

    def construct_graph(self):
        for u,v in self.edges:
            self.graph[u][v], self.graph[v][u] = True, True

    def dfs_visit(self, u):
        self.color[u]='G' # G for Gray
        for i in range(0, self.node):
            if self.graph[u][i]==True and self.color[i]=='W':
                self.parent[i]=u
                self.dfs_visit(i)
        self.color[u]='B' # B for black

    def dfs_traversal(self):
        for i in range(0,self.node):
            if self.color[i]=='W': # W for white
                self.dfs_visit(i)

    def print_path(self, source, destination):
        if destination==source:
            print destination,
        elif self.parent[destination] == -1:
            print "No Path"
        else:
            self.print_path(source, self.parent[destination])
            print "-> ",destination,

node = 8 # 8 nodes from 0 to 7
edges =[(0,1),(0,3),(1,2),(1,5),(2,7),(3,4),(3,6),(4,5),(5,7)] # bi-directional edge

dfs = DFS(node, edges)
dfs.print_path(0, 7)
print ""
dfs.print_path(2, 5)
print ""
dfs.print_path(0, 4)