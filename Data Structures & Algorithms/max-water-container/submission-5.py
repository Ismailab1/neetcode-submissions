class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1

        max_water = -1

        while lp < rp:
            curr_water = (rp - lp) * min(heights[rp], heights[lp])

            max_water = max(max_water, curr_water)

            if heights[rp] > heights[lp]:
                lp += 1
            
            else:
                rp -= 1
        
        return max_water