class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        triplet = set()

        for i in range(len(nums)):

            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            if nums[i] > 0 or i >= (len(nums)-2):
                break
            
            j = i + 1
            k = len(nums)-1

            while j < k:

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                elif nums[i] + nums[j] + nums[k] >0:
                    k -=1
                
                else:
                    j+=1
        return [list(x) for x in triplet]
        

                