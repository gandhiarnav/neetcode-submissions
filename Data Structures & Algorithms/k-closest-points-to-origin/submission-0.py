import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        
        for i,j in points:
            d = ((0-i)**2 + (0-j)**2)**0.5
            heapq.heappush(dis,(d,[i,j]))

        res = []
        for i in range(k):
            res.append(heapq.heappop(dis)[1])
        return res
        

        