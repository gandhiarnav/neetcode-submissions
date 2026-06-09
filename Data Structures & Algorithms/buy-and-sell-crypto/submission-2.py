class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr=0
        r=len(prices)-1
        m=0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                curr = prices[j]-prices[i]
                if curr>profit:
                    profit=curr
                print(curr)
        return profit
        
