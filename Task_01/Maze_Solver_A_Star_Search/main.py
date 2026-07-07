import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g_cost = 0
        self.h_cost = 0
        self.f_cost = 0
    
    def __lt__(self, other):
        return self.f_cost < other.f_cost

maze = [
    ['S', '.', '.', '#', '.'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', 'G', '.']
]

rows = len(maze)
cols = len(maze[0])

start = None
goal = None

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start = (i, j)
        if maze[i][j] == 'G':
            goal = (i, j)

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def get_neighbors(position):
    directions = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1)
    ]
    
    neighbors = []
    
    row, col = position

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if (
            0 <= new_row < rows and 0 <= new_col < cols
        ):
            
            if maze[new_row][new_col] != '#':
                neighbors.append((new_row, new_col))
    return neighbors

def reconstruct_path(node):
    path = []
    while node is not None:
        path.append(node.position)
        node = node.parent
    
    return path[::-1]

def a_star(start, goal):
    open_list = []
    closed_list = set()
    
    start_node = Node(start)
    start_node.g_cost = 0
    start_node.h_cost = heuristic(start, goal)
    start_node.f_cost = start_node.g_cost + start_node.h_cost
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        current_position = current_node.position

        if current_position == goal:
            return reconstruct_path(current_node)
        
        closed_list.add(current_position)

        for neighbor in get_neighbors(current_position):
            if neighbor in closed_list:
                continue
            
            neighbor_node = Node(neighbor, current_node)
            neighbor_node.g_cost = current_node.g_cost + 1
            neighbor_node.h_cost = heuristic(neighbor, goal)
            neighbor_node.f_cost = neighbor_node.g_cost + neighbor_node.h_cost
            heapq.heappush(open_list, neighbor_node)
    return None     

def visualize(path):
    display = []

    for row in maze:
        display.append(row.copy())
    
    if path:
        for position in path:
            r, c = position
            if display[r][c] not in ['S', 'G']:
                display[r][c] = '*'
    
    for row in display:
        print(" ".join(row))

solution = a_star(start, goal)
print("\nOriginal Maze:")
visualize(None)

if solution:
    print("\nShortest Path:")
    print(solution)
    print("\nPath Length:", len(solution)-1)
    print("\nSolved Maze:")
    visualize(solution)

else:
    print("\nNo path exists between Start and Goal")
