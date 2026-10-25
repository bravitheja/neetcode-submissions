class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])


        def dfs(i, j):
            if i <0 or i>=m or j <0 or j >=n or grid[i][j] == '0':
                return
            
            directions = (
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1)
            )

            grid[i][j] = '0'

            for x,y in directions:
                dfs(x, y)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count +=1
        return count
