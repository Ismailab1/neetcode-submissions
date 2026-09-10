from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize the result array with 1s
        result = [1] * len(nums)

        # Step 2: Calculate prefix products
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Step 3: Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        # Step 4: Return the result
        return result
