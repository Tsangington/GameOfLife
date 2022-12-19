import copy

grid = [[0,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,0]]
heatmapGrid = []

def heatmap(grid):
    for y in range(len(grid)):
        array = []
        for x in range(len(grid[y])):
            array.append(check_neighbours(grid, x, y))
        heatmapGrid.append(array)
    
    for rows in heatmapGrid:
        print(rows)


def check_neighbours(grid, x, y):
    total = 0
    neighbours = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),           (0, 1),
                   (1, -1),  (1, 0),  (1, 1)]
    for neighbour in neighbours: #try does not deem [-1] out of range.
        try:
            if y+neighbour[0] < 0 or x+neighbour[1] < 0: #negative, therefore out of bounds
                pass
            elif grid[y+neighbour[0]][x+neighbour[1]] == 1:
                total +=1
        except IndexError:
            pass
    return(total)

def next_iteration(grid):
    nextIterationGrid = copy.deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            neighbours = check_neighbours(grid, x, y)

            if (neighbours == 2 or neighbours == 3) and (grid[y][x] == 1):
                nextIterationGrid[y][x] = 1
            elif neighbours == 3 and grid[y][x] == 0:
                nextIterationGrid[y][x] = 1
            else:
                nextIterationGrid[y][x] = 0
                
    for rows in nextIterationGrid:
        print(rows)


next_iteration(grid)
