class Graph():
    def __init__(self,n): #n = no. of nodes
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def create_edges(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    
    def dfs_util(self, src, visited, result):
        result.append(src+1)
        visited[src] = True
        for node in self.adj[src]:
            if not visited[node]:
                self.dfs_util(node,visited,result)
    
    def DFS(self,src):
        visited = [False] * self.n
        result = []
        self.dfs_util(src, visited, result)
        return result

n = int(input("enter the number of nodes: "))
g = Graph(n)
m = int(input("enter the number of edges: "))
for i in range(m):
    x,y = map(int,input('Enter edge(x y): ').split())
    g.create_edges(x,y)
src = int(input("enter the starting node for DFS: "))
result = g.DFS(src-1)
print('DFS Traversal: ',result)


        