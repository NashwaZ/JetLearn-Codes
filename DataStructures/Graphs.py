class Graph():
    def __init__(self,limit):
        self.limit = 10
        self.adj_neighbours = [[]* self.limit for i in range(self.limit)]
    
    def create_neighbours(self, n1, n2):
        self.adj_neighbours[n1].append(n2)
        self.adj_neighbours[n2].append(n1)

    def bfs(self,start_point): #breadth first search
        visited = [False]*self.limit
        visited_sequence = []
        queue = [start_point]
        visited[start_point] = True
        while len(queue) > 0:
            visited_neighbour = queue.pop(0)
            visited_sequence.append(visited_neighbour)
            for neighbour in self.adj_neighbours[start_point]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour]= True
        

        print(visited_sequence)

graph = Graph(10)
graph.create_neighbours(1,2)
graph.create_neighbours(3,6)
graph.create_neighbours(4,2)
graph.create_neighbours(3,9)
graph.create_neighbours(1,5)
graph.create_neighbours(0,2)
graph.create_neighbours(7,0)

print(graph.adj_neighbours)


graph.bfs(0)

