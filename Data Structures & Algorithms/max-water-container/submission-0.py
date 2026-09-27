class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water = 0

        i = 0
        n = len(heights)-1

        while i < n:

            max_water = max(max_water,
            (n-i)*min(heights[i],heights[n]))

            if heights[i] > heights[n]:
                n-=1
            else:
                i+=1
        return max_water