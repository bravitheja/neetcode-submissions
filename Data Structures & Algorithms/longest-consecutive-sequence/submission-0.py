class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)

        max_length = 0

        for num in set_:
            
            if (num-1) not in set_:
                current = num+1
                count = 1

                while current in set_:
                    current += 1
                    count += 1

                max_length = max(count, max_length)
        return max_length