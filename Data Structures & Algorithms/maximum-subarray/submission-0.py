class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Checsk if the array exists
        if not nums:
            return 0

        # Initializes the result and the subarray to the first element
        res = nums[0]
        maxEnding = nums[0]

        # Starts the loop to determine 
        # the best choice of either continuing a sub array for starting a new subarray
        for i in range(1, len(nums)):
            # Either continues with the subarray or starts a new one based off the sum
            maxEnding = max(maxEnding + nums[i], nums[i])

            # Stores the maximum sum of the subarray
            res = max(res, maxEnding)
        
        # Returns teh maximum sum
        return res