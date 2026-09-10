class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If the string is nonexistent, we return 0 with a runtime of O(1)
        if not s:
            return 0
        
        # If the string is full of duplicates, we return 1 with a runtime of O(N) size
        if all(element == s[0] for element in s):
            return 1
        
        # Tracks the longest substring size
        longest_substring_size = 1
        
        # Tracks the current substring
        substring = {}
        left = 0

        # Iterates through the string in O(n) time
        for right, ch in enumerate(s):
            # If the current character is in the substring, we update the position of left
            # to the recorded position of the duplicate character from the substring
            if ch in substring and substring[ch] >= left:
                left = substring[ch] + 1
            # We add the current character position to the substring
            substring[ch] = right
            # We compare the current length of the substring to the current 
            # longest length we have recorded for the solution
            longest_substring_size = max(longest_substring_size, right - left + 1)
        # We return the longest substring size after iterating through the entire string    
        return longest_substring_size

        # Time complexity: O(n) time as we only iterate through the entire string once
        # Space complexity: O(min (n, sum of the alphabet size)) where the we store the entrie substring of the sum of every character in the alphabet
