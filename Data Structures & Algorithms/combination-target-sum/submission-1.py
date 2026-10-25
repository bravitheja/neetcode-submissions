class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        nums.sort()

        result = []
        temp = []

        def backtrack(index, current):

            if current == target:
                result.append(temp[::])
                return
            
            for i in range(index, len(nums)):
                
                if nums[i] > (target - current):
                    break
                
                temp.append(nums[i])
                # note this, we should use i not index. to prune the duplicates effectively.
                backtrack(i, current+nums[i])
                temp.pop()
        
        backtrack(0, 0)

        return result


        