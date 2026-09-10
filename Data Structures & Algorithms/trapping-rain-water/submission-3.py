class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        lp = 0
        rp = len(height) - 1

        leftMax = height[lp]
        rightMax = height[rp]

        result = 0

        while lp < rp:
            if leftMax < rightMax:
                lp += 1
                leftMax = max(leftMax, height[lp])
                result += leftMax - height[lp]

            else:
                rp -= 1
                rightMax = max(rightMax, height[rp])
                result += rightMax - height[rp]
        
        return result