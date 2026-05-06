import heapq

class a_star:
  def __init__(self, grid, start, goal):
    self.grid = grid
    self.start = start
    self.goal = goal
    self.rows = len(grid)
    self.coloumn = len(grid[0])

  def heuristic(self,node):
    return abs(node[0]-self.goal[0] + abs(node[1]-self.goal[1]))

  def nebighbors(self,node):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    result =[]
    for d in dirs:
      nebighbor = (node[0]+d[0],node[1]+d[1])
      if 0<=nebighbor[0]<self.rows and 0<=nebighbor[1]<self.coloumn:
        if self.grid[nebighbor[0]][nebighbor[1]]==0:
          result.append(nebighbor)
    return result
  
  def reconstruct_path(self, came_from, current):
    total_path = [current]
    while current in came_from:
      current = came_from[current]
      total_path.append(current)
    return total_path[::-1]
  
  def a_star_search(self):
    open_list=[]
    heapq.heappush(open_list,(0,self.start))
    came_from={}
    g_score={self.start:0}
    f_score={self.start:self.heuristic(self.start)}
    while open_list:
      current = heapq.heappop(open_list)[1]
      if current == self.goal:
        return self.reconstruct_path(came_from,current)
      
      for neighbor in self.nebighbors(current):
        tentaive_g_score = g_score[current]+1
        if neighbor not in g_score or tentaive_g_score < g_score[neighbor]:
          came_from[neighbor] = current
          g_score[neighbor]=tentaive_g_score
          f_score[neighbor]=tentaive_g_score + self.heuristic(neighbor)
          heapq.heappush(open_list,(f_score[neighbor],neighbor))
    return []

grid = [
  [0,1,0,1,0],
  [0,1,0,1,0],
  [0,0,0,1,0],
  [1,1,0,1,0],
  [0,0,0,0,0]
]

start, goal = (0,1),(4,0)
aStar = a_star(grid,start,goal)
print("\nPath from start to global:\n",aStar.a_star_search())