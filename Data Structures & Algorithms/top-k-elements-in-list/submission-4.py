from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = defaultdict(int)

        for i in nums:
            freq_map[i]+=1

        # bucket sort
        # max freq is len(nums)

        buckets = [ [] for _ in range(len(nums)+1)]

        for key, val in freq_map.items():
            buckets[val].append(key)
        
        answer = []
        for i in range(len(nums), -1, -1):
            if buckets[i]:
                answer.extend(buckets[i])

        return answer[:k]

        