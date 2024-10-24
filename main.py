import time

grid = []

def gridmaker(t):
  for i in range(30):
    y = []
    for i in range(58):
      y.append("-")
    t.append(y)
    
gridmaker(grid)

def printGrid(grid):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      print(str(grid[i][j]), end="")
    print("")
  
def PopCheck(grid):
  newGrid = []
  gridmaker(newGrid)
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      neighborCells = 0
      if grid[i][j] == 'o' or grid[i][j] == '-':
        
        if i+1 < len(grid) and grid[i+1][j] == 'o':
          neighborCells += 1
        if i-1 > 0 and grid[i-1][j] == 'o':
          neighborCells += 1
        if j+1 < len(grid[i]) and grid[i][j+1] == 'o':
          neighborCells += 1
        if j-1 > 0 and grid[i][j-1] =='o':
          neighborCells += 1
        if j+1 < len(grid[i]) and i+1 < len(grid) and grid[i+1][j+1] == 'o':
          neighborCells += 1
        if j-1 > 0 and i-1 > 0 and grid[i-1][j-1] == 'o':
          neighborCells += 1
        if j+1 < len(grid[i]) and i-1 > 0 and grid[i-1][j+1] == 'o':
          neighborCells += 1
        if j-1 > 0 and i+1 < len(grid) and grid[i+1][j-1] == 'o':
          neighborCells += 1
      
      if grid[i][j] == 'o':
        if neighborCells > 3:
          newGrid[i][j] = '-'
        elif neighborCells > 1:
          newGrid[i][j] = 'o'
        else:
          newGrid[i][j] = '-'
      else:
        if neighborCells == 3:
          newGrid[i][j] = 'o'
        else:
          newGrid[i][j] = '-'
  return newGrid

  
f = open("design.in", "r")

fLines = f.readlines()

cords = []

for i in fLines:
  i = [int(x)for x in i.split()]
  cords.append(i)
print(cords)
  


for i in range(len(cords)):
  x = cords[i][0]
  y = cords[i][1]
  grid[x][y] = 'o'
  
for i in range(len(grid)):
  for j in range(len(grid[i])):
    print(str(grid[i][j]), end="")
  print("")

for i in range(100):
  print("\033c")
  grid = PopCheck(grid)
  printGrid(grid)
  time.sleep(0.5)
