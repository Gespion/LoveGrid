import copy

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#temp_grid = copy.deepcopy(grid) #9x6 --> #6x9

#print(len(grid)) --> x: 9
#print(len(grid[0])) --> y: 6
#print(len(grid[0][0])) --> z: 1

love_grid = [['0' for y in range(len(grid))] for x in range(len(grid[0]))]

#print(len(love_grid)) #--> x: 6
#print(len(love_grid[0])) #--> y: 9
#print(len(love_grid[0][0])) # --> z: 1

# Rotate grid to 90°
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 'O':
            love_grid[y][x] = '.'
        else:
            love_grid[y][x] = '+'

for x in range(len(love_grid)):
    for y in range(len(love_grid[0])):
        print(love_grid[x][y],end=' ')
    print()