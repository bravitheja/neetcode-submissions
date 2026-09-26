from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        map_anagrams = defaultdict(list)

        for s in strs:
            map_anagrams["".join(sorted(s))].append(s)

        return list(map_anagrams.values())