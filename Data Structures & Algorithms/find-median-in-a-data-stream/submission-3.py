class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.call = 0

    def addNum(self, num: int) -> None:
        #put elements into maxheap
        heapq.heappush_max(self.maxheap,num)

        heapq.heappush(self.minheap,heapq.heappop_max(self.maxheap))
        
        #make equal
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush_max(self.maxheap,heapq.heappop(self.minheap))

        print("min heap:",self.minheap)
        print("max heap:",self.maxheap)
        self.call+=1


    def findMedian(self) -> float:
        l = len(self.minheap) + len(self.maxheap)
        
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        return (self.minheap[0] + self.maxheap[0])/2
    
        