class Solution:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = None
    
    def prepare_prefix_tree(self, words):

        root = self.TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = self.TrieNode()
                node = node.children[ch]
            node.word = word
        return root

        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = self.prepare_prefix_tree(words)

        m = len(board)
        n = len(board[0])

        result = set()

        def explore(i, j, node):
            if i <0 or i >= m or j <0 or j >= n or board[i][j] not in node.children:
                return None
            
            nonlocal result
            ch = board[i][j]

            if node.children[ch].word:
                result.add(node.children[ch].word)


            board[i][j] = '#'

            directions = ((i+1,j), (i-1, j), (i, j+1), (i, j-1))
            for x,y in directions:
                explore(x,y, node.children[ch])
            
            board[i][j] = ch
            
        for i in range(m):
            for j in range(n):
                explore(i, j, root)
        
        return list(result)

        