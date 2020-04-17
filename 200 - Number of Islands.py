class Solution:
# @param grid, a list of list of characters
# @return an integer
def numIslands(self, grid):
    if grid == []:
        return 0
        
    row = len(grid)
    col = len(grid[0])
    used = []
    for i in range(row):
        used.append([False] * col)
    
    count = 0
    for i in range(row):
        for j in range(col):
            num = self.dfs(grid, used, row, col, i, j)
            if num > 0:
                count += 1
    return count
    
def dfs(self, grid, used, row, col, x, y):
    if grid[x][y] == '0' or used[x][y]:
        return 0
    used[x][y] = True
    
    num = 1
    if x != 0:
        num += self.dfs(grid, used, row, col, x - 1, y)
    if x != row - 1:
        num += self.dfs(grid, used, row, col, x + 1, y)
    if y != 0:
        num += self.dfs(grid, used, row, col, x, y - 1)
    if y != col - 1:
        num += self.dfs(grid, used, row, col, x, y + 1)
    return num