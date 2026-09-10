class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Tracks each sequence and the length of the sequence using a set
        sequence = set(nums)
        longest = 0
        
        # Step 2: Track the longest sequence starting from the curent num and compae the length of each sequence
        for num in sequence:
            # Step 2.1 Starts the sequence at length 1 while making sure that nums that were part of another sequence do not start another loop
            if (num - 1) not in sequence:
                length = 1
                # Step 2.2: Continues the sequence as long as there is num+1 existing in the set
                while (num + length) in sequence:
                    length += 1
                # Step 2.3: Compares the length of the current sequence and the longest sequence
                longest = max(longest, length)
        return longest