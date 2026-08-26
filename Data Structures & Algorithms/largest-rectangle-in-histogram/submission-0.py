class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                start, height = stack.pop()
                maxArea = max(maxArea, height * (i - start))

            stack.append([start, h])
        print(stack)
        while stack:
            start, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - start))
            
        return maxArea
            
