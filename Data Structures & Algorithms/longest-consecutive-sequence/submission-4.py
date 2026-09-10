class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums) # storsn nums in a set to eliminate duplicates and find the sequence easier
        longest = 0

        for num in sequence: # checks each num in the set
            if (num - 1) not in sequence: # if the previous of num is not in the set, then it is the start of a new sequence
                length = 1 # starts the length of the sequence at 1
                while (num + length) in sequence: # checks for each character after num to see if the sequence continues
                    length += 1 # iterates the length of the sequence by one
                longest = max(longest, length) # checks max length of the sequence by the current length and by the previous stored longest sequence
        
        return longest # returns the longest length of the consecutive nums