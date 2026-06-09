class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]
        stone1,stone2 = 0,0
        res_stone = 0
        heapq.heapify_max(stones)
        while len(stones) > 2:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 == stone2:
                continue
            else:
                res_stone = max(stone1,stone2) - min(stone1,stone2)
                print(res_stone)
                heapq.heappush_max(stones,res_stone)
        if len(stones) == 1:
            return stones[0]
        res_stone = max(stones[0],stones[1]) - min(stones[0],stones[1])
        return res_stone

    
        