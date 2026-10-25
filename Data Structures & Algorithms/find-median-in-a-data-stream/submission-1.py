import heapq

class MedianFinder:

    def __init__(self):
        """
        two heaps:
        left half: max_heap:
        right half: min_heap:

        Median = take the heap which has max length of both heaps. extract top element thats median when uneven lengths. 
        if both are equal lengths then its average of both tops.
        """

        self.max_heap = []
        self.min_heap = []

        

    def addNum(self, num: int) -> None:

        left = self.max_heap[0]*(-1) if len(self.max_heap) else float('-inf')

        if num < left:
            heapq.heappush(self.max_heap, num*(-1))
        else:
            heapq.heappush(self.min_heap, num)

        while len(self.max_heap) > len(self.min_heap):
            temp = heapq.heappop(self.max_heap) * (-1)
            heapq.heappush(self.min_heap, temp)
        
        while (len(self.min_heap) - 1) > len(self.max_heap):
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, temp*-1)
        

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0]*(-1)+self.min_heap[0])/2
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]*(-1)
        else:
            return self.min_heap[0]

        
        