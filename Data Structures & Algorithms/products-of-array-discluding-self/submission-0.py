class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        suffix = [1] * len(nums)
        prefix = [1] * len(nums)

        n = len(nums)
        for i in range(1, len(nums)):

            prefix[i] = prefix[i-1] * nums[i-1]

            suffix[n-i-1] = suffix[n-i]*nums[n-i]

        for i in range(0, len(nums)):
            nums[i] = prefix[i] * suffix[i]
        
        return nums