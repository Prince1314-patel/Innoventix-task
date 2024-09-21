import heapq
import numpy as np

class PuzzleState:
    def __init__(self, board, parent=None, move=None, depth=0, cost=0):
        self.board = np.array(board)
        self.parent = parent
        self.move = move
        self.depth = depth  # g(n), actual cost
        self.cost = cost    # f(n) = g(n) + h(n)
    
    # Define goal state
    def is_goal(self):
        return np.array_equal(self.board, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]))
    
    # Get empty space position
    def find_empty(self):
        return np.argwhere(self.board == 0)[0]
    
    # Compute Manhattan Distance (h(n))
    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i, j] != 0:
                    goal_x, goal_y = divmod(self.board[i, j] - 1, 3)
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance
    
    # Get neighbors by moving the blank space
    def get_neighbors(self):
        neighbors = []
        x, y = self.find_empty()
        possible_moves = [
            (x-1, y), (x+1, y), (x, y-1), (x, y+1)  # Up, Down, Left, Right
        ]
        move_names = ["Up", "Down", "Left", "Right"]
        
        for move, (nx, ny) in zip(move_names, possible_moves):
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = self.board.copy()
                new_board[x, y], new_board[nx, ny] = new_board[nx, ny], new_board[x, y]
                neighbors.append(PuzzleState(new_board, parent=self, move=move, depth=self.depth + 1))
        return neighbors

    # A* comparison (priority based on f(n) = g(n) + h(n))
    def __lt__(self, other):
        return self.cost < other.cost

def astar_solver(start_board):
    # Initialize the start state and heap queue
    start_state = PuzzleState(start_board)
    start_state.cost = start_state.depth + start_state.manhattan_distance()  # f(n) = g(n) + h(n)
    
    # Priority queue to store (f(n), state) and visited set
    open_list = []
    heapq.heappush(open_list, start_state)
    
    visited = set()
    visited.add(str(start_state.board))
    
    while open_list:
        current_state = heapq.heappop(open_list)
        
        # Check if we reached the goal state
        if current_state.is_goal():
            return reconstruct_path(current_state)
        
        # Explore neighbors
        for neighbor in current_state.get_neighbors():
            if str(neighbor.board) not in visited:
                neighbor.cost = neighbor.depth + neighbor.manhattan_distance()
                heapq.heappush(open_list, neighbor)
                visited.add(str(neighbor.board))
    
    return None  # No solution found

# Reconstruct the path by backtracking
def reconstruct_path(state):
    path = []
    while state.parent is not None:
        path.append(state.move)
        state = state.parent
    return path[::-1]  # Reverse the path to get the correct order

# Example: Scrambled board
start_board = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = astar_solver(start_board)

if solution:
    print(f"Solved in {len(solution)} moves: {solution}")
else:
    print("No solution found.")
