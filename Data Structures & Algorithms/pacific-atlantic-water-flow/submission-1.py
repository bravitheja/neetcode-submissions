class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        reverse DFS
        """
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        invalid = lambda a, b: a<0 or a>=rows or b<0 or b>=cols

        def dfs(x,y, visited):
            if (x,y) in visited or invalid(x,y):
                return
            
            visited.add((x,y))

            directions = (
                (x+1,y),
                (x-1,y),
                (x,y+1),
                (x,y-1)
            )

            for a,b in directions:
                if (not invalid(a,b)) and heights[a][b]>=heights[x][y]:
                    dfs(a,b, visited)
            
        # who can reach pacific ocean: top row and left column
        
        # top row
        for i in range(cols):
            dfs(0, i, pacific)
        
        # left column
        for i in range(rows):
            dfs(i, 0, pacific)
        

        # who can reach atlantic occean: bottom row, right column

        # bottom row:
        for i in range(cols):
            dfs(rows-1, i, atlantic)
        
        # right column
        for i in range(rows):
            dfs(i, cols-1, atlantic)
        
        return [
            [i,j]
            for i in range(rows)
            for j in range(cols)
            if (i,j) in pacific and (i,j) in atlantic
        ]
