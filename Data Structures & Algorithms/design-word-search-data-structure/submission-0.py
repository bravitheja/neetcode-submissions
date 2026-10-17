class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            ch = word[index]

            if ch == '.':
                for temp in node.children.values():
                    if dfs(index+1, temp):
                        return True
                return False
            
            elif ch not in node.children:
                return False
            
            return dfs(index+1, node.children[ch])
        return dfs(0, self.root)
        
