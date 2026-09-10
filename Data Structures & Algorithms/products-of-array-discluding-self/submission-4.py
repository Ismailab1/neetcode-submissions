class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1's to ensure
        # it can be used for our multiplications
        res = [1] * len(nums)

        # Set the prefix to start at one then multiply itself with
        # every number it encounters in nums. Then save it to the
        # result array 
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Set the postfix to start at one then multiply itself with
        # every number it encounters in nums. Then save it to the
        # result array 
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        # Return the result array
        return res
