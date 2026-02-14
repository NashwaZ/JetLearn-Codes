class Graph():
    def __init__(self, n):
        self.n = n
        self.adj = {i:[]for i in range(n)}
        print(self.adj)

    def create_edges(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)
        print(self.adj)

    #usinfgdfs for checking all the connected components

    def dfs_utiliy(self, node, visited):
        visited[node] = True
        for neigbour in self.adj[node]:
            self.dfs(neigbour,visited)

    def DFS(self):
        visited = [False] * self.n
        count = 0
        for i in range(self.n):
            if not visited[i]:
                count+=1
                self.dfs_utiliy(i, visited)
        return count
    
    #using dfs for cycle detection

    def dfs_cycle(self, node, parent, visited):
        visited[node] = True
        for neighbour in self.adj[node]:
            if not visited[neighbour]:
                if self.dfs_cycle(neighbour, node, visited):
                    return True
            elif neighbour != parent:
                return True
        return False
    
    # detect cycle

    def has_cycle(self,visited):
        for i in range(self.n):
            if not visited[i]:
                if self.dfs_cycle(i, -1, visited):
                    return True
        return False






o = Graph(7)
o.create_edges(0,1)
o.create_edges(1,3)
o.create_edges(3,4)