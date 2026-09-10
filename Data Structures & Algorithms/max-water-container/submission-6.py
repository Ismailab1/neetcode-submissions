class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        maxArea = -1
        
        l = 0
        r = len(heights) - 1

        while l < r:
            maxArea = max(maxArea, min(heights[l], heights[r]) * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea