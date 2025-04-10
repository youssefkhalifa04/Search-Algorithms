import  random


def create_grid(size = 5 , num_obstacles = 3):
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append('-')
        grid.append(row)
    grid[0][0] = 's'
    grid[size-1][size-1] = 'T'
    for _ in range(num_obstacles):
        x,y =random.randint(0,size-1),random.randint(0,size-1)
        while grid[x][y] != '-':
            x,y = random.randint(0,size-1),random.randint(0,size-1)
        grid[x][y] = '0'
    return grid
def display(grid):
    for row in grid:
        print(' '.join(row))
    print()
def moveAgent(grid , start , target) :
    x , y = start
    tx , ty = target
    if x<tx and grid[x+1][y] != '0':
        x+= 1
    elif x>tx and grid[x-1][y] != '0':
        x-= 1
    elif y<ty and grid[x][y+1] != '0':
        y+= 1
    elif y>ty and grid[x][y-1] != '0':
        y-= 1
    return x , y
def simulate(grid):
    size = len(grid)
    start = (0,0)
    target = (size-1,size-1)
    #position actuelle de l'agent
    current_position = start
    print("Grille initiale")

    display(grid)
    step = 0
    while current_position != target:
        step += 1
        print(f"Etape {step}")
        newPosition = moveAgent(grid, current_position, target)
        grid[current_position[0]][current_position[1]] = '-'
        grid[newPosition[0]][newPosition[1]] = 's'
        current_position = newPosition
        display(grid)
    print("l'agent attenit la cible avec success")
grid = create_grid(size = 5 , num_obstacles = 3)
simulate(grid)






