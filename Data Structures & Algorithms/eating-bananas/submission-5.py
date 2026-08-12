import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = sum(piles)
        if s<=h:
            return 1
        l = 2
        r = max(piles)
        print(f"l,r={l,r}")
        
        while l<=r:
            mid = l + (r-l)//2
            # print(f"l,r={l,r}")
            # print(mid)
            hc = 0
            for n in piles:
                hc += math.ceil(n / mid)

            if hc<=h:
                res = mid
                r = mid -1

            elif hc>h:
                l = mid +1

        return res
            