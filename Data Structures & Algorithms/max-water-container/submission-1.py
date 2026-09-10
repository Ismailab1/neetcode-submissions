class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Sets up the pointers for setting up the container
        lp, rp = 0 , len(heights) - 1

        # Tracks the max amount of water in a possible container
        maxAmount = 0

        while lp <= rp:
            # Gets the current amount of water possible within a container
            currAmount = min(heights[lp], heights[rp]) * (rp - lp)

            # Compares the current amount to the max recorded amount
            # and stores the greater value
            maxAmount = max(maxAmount, currAmount)

            # Moves the left pointer if the barrier height is shorter
            if heights[lp] < heights[rp]:
                lp += 1
            
            # Moves the right pointer if the barrier height is shorter
            elif heights[lp] > heights[rp]:
                rp -= 1
            
            # If both are even, I move the left pointer
            else:
                lp += 1
            
        return maxAmount