

def bomberMan(n, grid):

    gridTiming = []
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid[0])):
            if grid[i][j] != ".":
                temp.append(1)
            else:
                temp.append(0)
        gridTiming.append(temp)

    grid = gridTiming

    def incrementTiming():
        counter = len(grid)
        counter1 = len(grid[0])
        arrTimeOut =[]
        for i in range(counter):
            for j in range(counter1):
                grid[i][j] += 1
                if grid[i][j] == 3:
                    arrTimeOut.append([i,j])
                    if i-1 > -1: arrTimeOut.append([i - 1,j])
                    if i+1 < counter: arrTimeOut.append([i + 1,j])
                    if j-1 > -1: arrTimeOut.append([i,j-1])
                    if j+1 < counter1: arrTimeOut.append([i,j+1])
        return arrTimeOut

    def explode(timedOut):
        counter = len(timedOut)
        for i in range(counter):
            x,y = timedOut[i]
            grid[x][y] = 0

    n = n % 4 + 4
    for i in range(2, n):
        arrTimedOut = incrementTiming()
        explode(arrTimedOut)

    gridTiming = []
    for i in range(len(grid)):
        temp = ""
        for j in range(len(grid[0])):
            if grid[i][j] == 0: temp += "."
            else: temp += "O"
        gridTiming.append(temp)

    return gridTiming


grid = [
    [".",".",".",".",".",".","."],
    [".",".",".",0,".",".","."],
    [".",".",".",".",0,".","."],
    [".",".",".",".",".",".","."],
    [0,0,".",".",".",".","."],
    [0,0,".",".",".",".","."]
]
"""

grid = [
    [".", ".", "."],
    [".", 0, "."],
    [".", ".", "."]
]
"""

print(bomberMan(7, grid))



