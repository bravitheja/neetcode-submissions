from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        freq_map = defaultdict(int)
        max_freq = 0
        
        for right in range(len(s)):
            freq_map[s[right]] += 1
            max_freq = max(max_freq, freq_map[s[right]])
            while (right - left + 1) - max_freq > k:
                freq_map[s[left]]-=1
                left+=1

        return len(s)-left