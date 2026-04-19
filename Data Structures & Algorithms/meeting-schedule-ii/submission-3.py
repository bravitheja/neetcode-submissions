"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
[(0,40),(5,10),(15,20)]

0, 5, 15
10, 20, 40

1, 
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_time = [interval.start for interval in intervals]
        end_time = [interval.end for interval in intervals]
        start_time.sort()
        end_time.sort()

        count = 0
        max_count = 0
        i,j = 0, 0
        while i < len(start_time):
            if start_time[i] < end_time[j]:
                count +=1
                max_count = max(max_count, count)
                i += 1
            else:
                count -= 1
                j += 1
            
        return max_count




