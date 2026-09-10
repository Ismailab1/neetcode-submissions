class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        # Tracks the longest substring size
        longest_substring_size = 1
        
        # Tracks the current substring
        substring = deque()

        # Iterates through the string in O(n) time
        for right in range(len(s)):
            # If the current character is in the substring, we clear the substring
            while s[right] in substring:
                substring.popleft()
            # We add the current character to the substring
            substring.append(s[right])
            # We compare the current length of the substring to the current 
            # longest length we have recorded for the solution
            longest_substring_size = max(longest_substring_size, len(substring))
        # We return the longest substring size after iterating through the entire string    
        return longest_substring_size

        # Time complexity: O(n) time as we only iterate through the string once
        # Space complexity: O(n) space as we eventually hav ethe set store every part of the string
