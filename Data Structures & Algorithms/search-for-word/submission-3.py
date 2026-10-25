class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not word:
            return True

        if not board:
            return False

        m = len(board)
        n = len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
            
            directions = (
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1)
            )
            current = board[i][j]
            board[i][j] = '#'
            for x, y in directions:
                if dfs(x,y, index+1):
                    board[i][j] = current
                    return True
            
            board[i][j] = current
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
