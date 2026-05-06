def print_board(board):
  for row in board:
    print(" ".join("Q" if col else "." for col in row))
  print()

def is_safe(board, row, col, n):
  for i in range(row):
    if board[i][col]:return False
  for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
    if board[i][j]:return False
  for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
    if board[i][j]:return False
  return True


def solve_bt(board,row,n):
  if row == n:
    print_board(board)
    return True
  for col in range(n):
    if is_safe(board,row,col,n):
      board[row][col]=True
      if solve_bt(board, row+1, n): return True
      board[row][col]=False
  return False     

def solve_bnb(row,n,cols,d1,d2,board):
  if row == n:
    print_board(board)
    return True
  for col in range(n):
    if not (cols[col] or d1[row+col] or d2[row-col+(n-1)]):
      board[row][col] = cols[col] = d1[row+col] = d2[row-col+(n-1)] = True
      if solve_bnb(row+1,n,cols,d1,d2,board):return True
      board[row][col]=cols[col]=d1[row+col]=d2[row-col+(n-1)] = False
  return False

n=16
print("Backtracking:\n")
solve_bt([[False]*n for _ in range(n)],0,n)
print("Branch and Bound:\n")
solve_bnb(0,n,[False]*n,[False]*(2*n-1),[False]*(2*n-1),[[False]*n for _ in range(n)])