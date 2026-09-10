class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: Empty array
        if not height:
            return 0

        # Sets up two pointers to keep track of the heights
        # in the array while also tracking the maximum height to store
        # water in the previous positions
        l , r = 0 , len(height) - 1
        leftMax, rightMax = height[l], height[r]
        
        res = 0

        while l < r:
            # For each pointer, we move the pointer by one position and store water into
            # the last position by using the diffirence between the max height and the current position.
            # If we reach a new max, no water will be added until the pointer
            # reaches a lower height
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res