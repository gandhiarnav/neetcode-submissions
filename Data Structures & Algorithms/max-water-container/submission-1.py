class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                dist=j-i
                if max_w < min(heights[i],heights[j])*dist:
                    max_w = min(heights[i],heights[j])*dist
                print(max_w)
        return max_w

