# # Template for backtracking using dfs

# class backtracking:
#     def __init__(self):
#         self.state = []    
        
#     def dfs(state):
#         res = []
#         if is_solution(state):
#             res.append(state[:]) # e.g. add a copy of the state to final result list
#             return

#         for choice in choices:
#             if valid(choice):
#                 state.add(choice) # make move
#                 dfs(state)
#                 state.remove(choice) # backtrack

def print_table(state, n):
  for row in range(n):
    for col in range(n):
      if [row, col] in state:
        print('X', end=" ")
      else:
        print('*', end=" ")
    print("")


def valid(row, col, state, n):
  not_valid_cell = set()
  for r, c in state:
    rr, cc = r, c
    while rr + 1 < n and cc + 1 < n:
      rr += 1
      cc += 1
      not_valid_cell.add((rr, cc))
    rr, cc = r, c
    while rr - 1 >= 0 and cc - 1 >= 0:
      rr -= 1
      cc -= 1
      not_valid_cell.add((rr, cc))
    rr, cc = r, c
    while rr - 1 >= 0 and cc + 1 < n:
      rr -= 1
      cc += 1
      not_valid_cell.add((rr, cc))
    rr, cc = r, c
    while rr + 1 < n and cc - 1 >= 0:
      rr += 1
      cc -= 1
      not_valid_cell.add((rr, cc))

  # print_table(state, n)
  # print('---------------')
  for r, c in state:
    for i in range(n):
      not_valid_cell.add((r, i))
      not_valid_cell.add((i, c))

  if (row, col) in not_valid_cell:
    return False
  
  return True

def helper(n, result, row, state):
  if row > n:
    return
  if n == len(state):
    result[0] += 1
    return

  for col in range(n):
    if valid(row, col, state, n):
      state.append([row, col])
      helper(n, result, row + 1, state)
      state.pop()


def solve_n_queens(n):
  result = [0]
  helper(n, result, 0, [])
  return result[0]

print(solve_n_queens(6))
        


