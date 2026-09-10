class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1

        ans = []

        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                curr *= nums[j]
            ans.append(curr)
        
        return ans