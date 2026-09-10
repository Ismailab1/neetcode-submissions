class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # 1-indexed array for answer

        prefix = 1 # starts the prefix at 1
        for i in range(len(nums)):
            res[i] = prefix # stores the prefix at current element
            prefix *= nums[i] # multiplies the prefix by the current element
        postfix = 1 # starts the postifx at 1
        for i in range(len(nums) - 1, -1, -1): # goes through the array reversed
            res[i] *= postfix # multiplies the postfix by the prefix
            postfix *= nums[i] # multiplies the prefix by the current element
        return res # returns the result