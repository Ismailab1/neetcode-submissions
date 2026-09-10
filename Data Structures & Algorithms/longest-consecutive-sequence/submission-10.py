class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sequence = set(nums)

        longest = 1

        for num in sequence:
            if num - 1 not in sequence:
                length = 0
            
                while (num + length) in sequence:
                    length += 1
                
                longest = max(longest, length)

        return longest