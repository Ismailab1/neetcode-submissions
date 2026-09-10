class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1

        sequence = set(nums)

        for num in sequence:
            if (num - 1) not in sequence:
                length = 0
                
                while num + length in sequence:
                    length += 1

                longest = max(longest, length)
        
        return longest