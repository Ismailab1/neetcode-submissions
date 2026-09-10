class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        count = 1
        final_count = 1

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == (nums[i - 1] + 1):
                count += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                count = 1
            final_count = max(final_count, count)
        
        return final_count