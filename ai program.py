from collections import deque

def bfs(start_state):
    target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    dq = deque([start_state])
    visited = {tuple(start_state): None}
    
    while dq:
        state = dq.popleft()
        if state == target:
            # Backtrack to form path
            path = []
            while state:
                path.append(state)
                state = visited[tuple(state)]
            return path[::-1]
        
        zero = state.index(0)
        row, col = divmod(zero, 3)
        
        for move in (-3, 3, -1, 1):  # Up, Down, Left, Right
            new_index = zero + move
            if 0 <= new_index < 9:
                new_row, new_col = divmod(new_index, 3)
                # Check if move is valid (no wrap-around)
                if abs(row - new_row) + abs(col - new_col) == 1:
                    neighbor = state[:]
                    neighbor[zero], neighbor[new_index] = neighbor[new_index], neighbor[zero]
                    if tuple(neighbor) not in visited:
                        visited[tuple(neighbor)] = state
                        dq.append(neighbor)
    return None

def printSolution(path):
    for state in path:
        print("\n".join(' '.join(map(str, state[i:i+3])) for i in range(0, 9, 3)), end="\n-----\n")

# Example Usage
startState = [1, 3, 0, 6, 8, 4, 7, 5, 2]
solution = bfs(startState)
if solution:
    printSolution(solution)
    print(f"Solved in {len(solution) - 1} moves.")
else:
    print("No solution found.")
