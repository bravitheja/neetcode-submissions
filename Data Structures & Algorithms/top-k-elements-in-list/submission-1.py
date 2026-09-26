from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = defaultdict(int)

        for i in nums:
            freq_map[i]+=1

        freq_map = sorted(freq_map.items(), key = lambda item: item[1], reverse=True)

        return [x for x, y in freq_map[:k]]

        