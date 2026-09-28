class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        zxyzxyz

        sliding window plus last found char map
        """

        map_ = {}
        left = 0
        max_length = 0
        
        
        for i in range(len(s)):
            
            if s[i] in map_ and map_[s[i]] >= left:
                left = map_[s[i]] + 1
            
            map_[s[i]] = i
            max_length = max(max_length, i - left + 1)
        
        return max_length

        