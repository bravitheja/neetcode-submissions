class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        left = 0
        right = 5

        mid = 2
        
        [3,4,5,6,1,2]

        3 < 5: true
        left = 2
        right = 5
        (2+5)//2 = 3
        mid = 3

        5<6
        left = 3
        right = 5
        mid = 3+5//2 = 4

        6<1: False
        right = mid = 4
        
        3<4
        mid = 3+4//2 =3

nums=[4,5,6,7]
mid = 1


        """

        left = 0
        right = len(nums)-1
        mid = 0
        answer = -1
        while left < right:
            mid = (left+right)//2
            # identify which half is sorted and apply binary search on that part only.

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

