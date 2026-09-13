class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        i = 0
        n = len(nums)

        while i < n:
            nums.append(nums[i])
            i += 1

        return nums