class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0

        while l < r:
            left, right = heights[l], heights[r]
            ans = max(ans, min(left, right) * (r - l))

            if left <= right:
                while l < r and heights[l] <= left:
                    l += 1
            else:
                while l < r and heights[r] <= right:
                    r -= 1

        return ans