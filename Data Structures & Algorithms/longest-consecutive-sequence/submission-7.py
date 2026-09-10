class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If there are no elements in nums
        # we return 0 due to no possible sequence
        if not nums:
            return 0
        
        # Stores the nums array in a set  for O(1) lookup
        # of every number in the array with no duplicates
        # and to search for each corresponding letter
        sequence = set(nums)

        # Starts the sequence at 1, which will be our answer if
        # no sequence appears
        longest = 1

        # Looks at each num in sequence and starts the longest counter if the
        # current num is not in a sequence already
        for num in sequence:
            if (num - 1) not in sequence:
                length = 0

                # Increases the length each time we a number that
                # continues the sequence
                while (num + length) in sequence:
                    length += 1
                
                # Stores the maximum value between the previously recorded longest sequence
                # and the sequence we just recorded
                longest = max(longest, length)

        # Returns the longest sequence we found in nums
        return longest