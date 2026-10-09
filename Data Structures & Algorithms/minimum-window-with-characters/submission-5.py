from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """
        compute freq map of t.
        then we need to have one on going freq map 
        of current window on s. current_map

        we need to slide the window until it fails. we need to store min length, start and end index of satisfied window 

        trace out:
        s="ADOBECODEBANC"
        t="ABC"

        freq_map: {A:1, B: 1, C:1}
        current:
        {A:1, B:2, C:1 }
        left = 1
        """

        min_length = float('inf')
        start = end = 0
        freq_map = defaultdict(int)
        current_map = defaultdict(int)

        formed = 0
        
        for ch in t:
            freq_map[ch]+=1

        required = len(freq_map)
        
        left = 0
        for right in range(len(s)):

            if s[right] in freq_map: 
                current_map[s[right]]+=1
                if freq_map[s[right]] == current_map[s[right]]:
                    formed +=1

            while formed == required:

                if min_length >= (right - left + 1):
                    start = left
                    end = right+1
                    min_length = right - left + 1

                if s[left] in freq_map:
                    current_map[s[left]]-=1
                    if current_map[s[left]] < freq_map[s[left]]:
                        formed -=1


                left += 1

        print(min_length)
        return s[start:end]









