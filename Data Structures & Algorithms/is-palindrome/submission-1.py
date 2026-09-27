class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)-1

        i =0
        while i<n:
            while i< n and not s[i].isalnum():
                i +=1
            while i< n and not s[n].isalnum():
                n -=1
            if i< n and s[i].isalnum() and s[i].isalnum() and s[i].casefold()!=s[n].casefold():
                return False
            i+=1
            n-=1
        return True
        