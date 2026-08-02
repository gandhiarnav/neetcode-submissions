class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0

        while l < r:
            left, right = heights[l], heights[r]
            width = r - l

            if left < right:
                ans = max(ans, left * width)
                l += 1
            else:
                ans = max(ans, right * width)
                r -= 1

        return ans