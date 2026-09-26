class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        visited = {}

        for idx, num in enumerate(nums):
            x = target - num
            if x in visited:
                return [visited[x], idx]
            visited[num] = idx
        
        