from collections import defaultdict, deque

class Graph:
  def __init__(self):
    self.graph = defaultdict(list);
  def add_edge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def dfsRecursive(self, vertex, visitedNode=None):
    if visitedNode is None:
      visitedNode = set()
    visitedNode.add(vertex)
    print(vertex,end=" ")
    for neighbour in self.graph[vertex]:
      if neighbour not in visitedNode:
        self.dfsRecursive(neighbour,visitedNode)

  def bfs(self,start):
    visited=set();
    queue = deque([start])
    visited.add(start);
    while queue:
      vertex = queue.popleft()
      print(vertex,end=" ")
      for neighbour in self.graph[vertex]:
        if neighbour not in visited:
          queue.append(neighbour);
          visited.add(neighbour);


g = Graph()
edges=[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(3,7),(4,8),(5,9),(6,10)]
for u,v in edges:
  g.add_edge(u,v)

print('depth first search starting from vertex 0 :')
g.dfsRecursive(0)
print('\nbreadth first search starting from vertex 0 :')
g.bfs(0)
