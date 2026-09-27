class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']':'['}

        stack = []

        for ch in s:

            if ch in ('(', '[', '{'):
                stack.append(ch)
            
            else:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                else:
                    stack.pop()    

        return not stack